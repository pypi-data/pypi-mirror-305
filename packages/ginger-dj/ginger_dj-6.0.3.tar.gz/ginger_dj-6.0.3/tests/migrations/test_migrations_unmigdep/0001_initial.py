from gingerdj.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            "Book",
            [
                ("id", models.AutoField(primary_key=True)),
            ],
        )
    ]
