# Generated by Django 2.1.11 on 2021-02-24 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_v2", "0010_pokemonformtype"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeEfficacyPast",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("damage_factor", models.IntegerField()),
                (
                    "damage_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="typeefficacypast_damage_type",
                        to="pokemon_v2.Type",
                    ),
                ),
                (
                    "generation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="typeefficacypast",
                        to="pokemon_v2.Generation",
                    ),
                ),
                (
                    "target_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="typeefficacypast_target_type",
                        to="pokemon_v2.Type",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="typeefficacy",
            name="damage_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="typeefficacy_damage_type",
                to="pokemon_v2.Type",
            ),
        ),
        migrations.AlterField(
            model_name="typeefficacy",
            name="target_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="typeefficacy_target_type",
                to="pokemon_v2.Type",
            ),
        ),
    ]
