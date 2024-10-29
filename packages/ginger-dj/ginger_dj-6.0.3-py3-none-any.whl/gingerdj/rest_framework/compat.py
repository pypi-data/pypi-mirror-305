"""
The `compat` module provides support for backwards compatibility with older
versions of Django/Python, and compatibility wrappers around optional packages.
"""

import gingerdj
from gingerdj.views.generic import View


def unicode_http_header(value):
    # Coerce HTTP header value to unicode.
    if isinstance(value, bytes):
        return value.decode("iso-8859-1")
    return value


# gingerdj.contrib.postgres requires psycopg2
try:
    from gingerdj.contrib.postgres import fields as postgres_fields
except ImportError:
    postgres_fields = None


# coreapi is required for CoreAPI schema generation
try:
    import coreapi
except ImportError:
    coreapi = None

# uritemplate is required for OpenAPI and CoreAPI schema generation
try:
    import uritemplate
except ImportError:
    uritemplate = None


# coreschema is optional
try:
    import coreschema
except ImportError:
    coreschema = None


# pyyaml is optional
try:
    import yaml
except ImportError:
    yaml = None

# inflection is optional
try:
    import inflection
except ImportError:
    inflection = None


# requests is optional
try:
    import requests
except ImportError:
    requests = None


# PATCH method is not implemented by Django
if "patch" not in View.http_method_names:
    View.http_method_names = View.http_method_names + ["patch"]


# Markdown is optional (version 3.0+ required)
try:
    import markdown

    HEADERID_EXT_PATH = "markdown.extensions.toc"
    LEVEL_PARAM = "baselevel"

    def apply_markdown(text):
        """
        Simple wrapper around :func:`markdown.markdown` to set the base level
        of '#' style headers to <h2>.
        """
        extensions = [HEADERID_EXT_PATH]
        extension_configs = {HEADERID_EXT_PATH: {LEVEL_PARAM: "2"}}
        md = markdown.Markdown(
            extensions=extensions, extension_configs=extension_configs
        )
        md_filter_add_syntax_highlight(md)
        return md.convert(text)

except ImportError:
    apply_markdown = None
    markdown = None


try:
    import pygments
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import TextLexer, get_lexer_by_name

    def pygments_highlight(text, lang, style):
        lexer = get_lexer_by_name(lang, stripall=False)
        formatter = HtmlFormatter(nowrap=True, style=style)
        return pygments.highlight(text, lexer, formatter)

    def pygments_css(style):
        formatter = HtmlFormatter(style=style)
        return formatter.get_style_defs(".highlight")

except ImportError:
    pygments = None

    def pygments_highlight(text, lang, style):
        return text

    def pygments_css(style):
        return None


if markdown is not None and pygments is not None:
    # starting from this blogpost and modified to support current markdown extensions API
    # https://zerokspot.com/weblog/2008/06/18/syntax-highlighting-in-markdown-with-pygments/

    import re

    from markdown.preprocessors import Preprocessor

    class CodeBlockPreprocessor(Preprocessor):
        pattern = re.compile(r"^\s*``` *([^\n]+)\n(.+?)^\s*```", re.M | re.S)

        formatter = HtmlFormatter()

        def run(self, lines):
            def repl(m):
                try:
                    lexer = get_lexer_by_name(m.group(1))
                except (ValueError, NameError):
                    lexer = TextLexer()
                code = m.group(2).replace("\t", "    ")
                code = pygments.highlight(code, lexer, self.formatter)
                code = (
                    code.replace("\n\n", "\n&nbsp;\n")
                    .replace("\n", "<br />")
                    .replace("\\@", "@")
                )
                return "\n\n%s\n\n" % code

            ret = self.pattern.sub(repl, "\n".join(lines))
            return ret.split("\n")

    def md_filter_add_syntax_highlight(md):
        md.preprocessors.register(CodeBlockPreprocessor(), "highlight", 40)
        return True

else:

    def md_filter_add_syntax_highlight(md):
        return False


if gingerdj.VERSION >= (5, 1):
    # Django 5.1+: use the stock ip_address_validators function
    # Note: Before Django 5.1, ip_address_validators returns a tuple containing
    #       1) the list of validators and 2) the error message. Starting from
    #       Django 5.1 ip_address_validators only returns the list of validators
    from gingerdj.core.validators import ip_address_validators
else:
    # Django <= 5.1: create a compatibility shim for ip_address_validators
    from gingerdj.core.validators import ip_address_validators as _ip_address_validators

    def ip_address_validators(protocol, unpack_ipv4):
        return _ip_address_validators(protocol, unpack_ipv4)[0]


# `separators` argument to `json.dumps()` differs between 2.x and 3.x
# See: https://bugs.python.org/issue22767
SHORT_SEPARATORS = (",", ":")
LONG_SEPARATORS = (", ", ": ")
INDENT_SEPARATORS = (",", ": ")
