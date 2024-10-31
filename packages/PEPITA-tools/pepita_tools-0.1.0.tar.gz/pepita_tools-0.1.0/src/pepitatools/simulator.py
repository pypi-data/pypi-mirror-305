# Imports
# Standard Library Imports
import random
from time import time


# External Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Local Imports
from . import dose_response, utils
from .configuration import get_config_setting


def add_noise(n, percent=0.05, standard_dev=5):
    standard_dev = standard_dev + n * percent
    return random.gauss(n, standard_dev)


def add_static_noise(n, standard_dev=5):
    return random.gauss(n, standard_dev)


def add_percent_noise(n, coefficient_variance=0.05):
    standard_dev = n * coefficient_variance
    return random.gauss(n, standard_dev)


def bliss_vs_loewe():
    cocktail_a = utils.Cocktail("A")
    cocktail_b = utils.Cocktail("B")
    cocktail_combo = utils.Cocktail(("A", "B"))

    df = pd.DataFrame(
        columns=[
            "simulation",
            "doseA",
            "doseB",
            "responseA",
            "responseB",
            "responseCombo",
            "EOB",
            "FIC",
        ]
    )

    for i in range(1000):
        model_a = dose_response.Model([], [], cocktail_a)
        model_a.b = random.uniform(0.5, 3)
        model_a.c = random.randint(6, 40)
        model_a.e = random.randint(5, 500)

        model_b = dose_response.Model([], [], cocktail_b)
        model_b.b = random.uniform(0.5, 3)
        model_b.c = random.randint(6, 40)
        model_b.e = random.randint(5, 500)

        ec50_a = model_a.effective_concentration(0.5)
        ec50_b = model_b.effective_concentration(0.5)

        model_a.xs = np.array([ec50_a / 4, ec50_a / 2, ec50_a, 2 * ec50_a])
        model_b.xs = np.array([ec50_b / 4, ec50_b / 2, ec50_b, 2 * ec50_b])

        model_a.ys = model_a.get_ys(model_a.xs)
        model_b.ys = model_b.get_ys(model_b.xs)

        model_combo = dose_response.Model(model_a.xs + model_b.xs, [], cocktail_combo)
        model_combo.b = random.uniform(0.5, 3)
        model_combo.c = random.randint(6, 40)
        model_combo.e = random.randint(5, 500)
        model_combo.ys = model_combo.get_ys(model_combo.xs)

        for a_x, b_x, combo_x, combo_y in zip(
            model_a.xs, model_b.xs, model_combo.xs, model_combo.ys
        ):
            model_combo.cocktail.ratio = utils.Ratio(a_x, b_x)
            eob = dose_response.get_bliss_ixn(
                combo_x, combo_y, model_a, model_b, model_combo
            )
            fic = dose_response.get_combo_FIC(
                1 - model_combo.get_pct_survival(xs=combo_x),
                model_a,
                model_b,
                model_combo,
                model_combo.cocktail.ratio,
            )

            df = df.append(
                {
                    "simulation": i,
                    "doseA": a_x,
                    "doseB": b_x,
                    "responseA": model_a.get_pct_survival(xs=a_x),
                    "responseB": model_b.get_pct_survival(xs=b_x),
                    "responseCombo": model_combo.get_pct_survival(xs=combo_x),
                    "EOB": eob,
                    "FIC": fic,
                },
                ignore_index=True,
            )

    df.to_csv("bliss_vs_loewe.csv", index=False)


def main():
    # simulate_noise()
    bliss_vs_loewe()


def simulate_noise():
    cocktail = utils.Cocktail("Test1")
    errors = {}

    for i in range(10000):
        model_real = dose_response.Model([], [], cocktail)
        model_real.b = random.uniform(0.5, 3)
        model_real.c = random.randint(6, 40)
        model_real.e = random.randint(5, 500)
        model_real.equation = lambda xs, b, c, e: dose_response.log_logistic_model(
            xs, b, c, 100, e
        )

        ec75_real = model_real.effective_concentration(0.75)

        model_real.xs = np.array(
            [0, ec75_real / 4, ec75_real / 2, ec75_real, 2 * ec75_real]
        )
        model_real.ys = model_real.get_ys(model_real.xs)

        noisy_ys = [add_noise(y) for y in model_real.ys]

        try:
            model_noisy = dose_response.Model(model_real.xs, noisy_ys, cocktail)
        except RuntimeError:
            # sometimes the random values yield an invalid result -- that's fine, move on
            continue

        ec25_real = model_real.effective_concentration(0.25)
        ec50_real = model_real.effective_concentration(0.5)
        ec90_real = model_real.effective_concentration(0.9)

        ec25_noisy = model_noisy.effective_concentration(0.25)
        ec50_noisy = model_noisy.effective_concentration(0.5)
        ec75_noisy = model_noisy.effective_concentration(0.75)
        ec90_noisy = model_noisy.effective_concentration(0.9)

        error_ec25 = abs(ec25_real - ec25_noisy) / ec25_real
        error_ec50 = abs(ec50_real - ec50_noisy) / ec50_real
        error_ec75 = abs(ec75_real - ec75_noisy) / ec75_real
        error_ec90 = abs(ec90_real - ec90_noisy) / ec90_real

        utils.put_multimap(errors, 25, error_ec25)
        utils.put_multimap(errors, 50, error_ec50)
        utils.put_multimap(errors, 75, error_ec75)
        utils.put_multimap(errors, 90, error_ec90)

    errors_df = pd.DataFrame(
        {
            "EC value": [key for key, values in errors.items() for _ in values],
            "Percent Error": [
                value for key, values in errors.items() for value in values
            ],
        }
    )

    fig = plt.figure()
    fig.set_size_inches(12, 8)
    fig.set_dpi(100)
    sns.histplot(
        data=errors_df,
        x="Percent Error",
        bins=128,
        common_norm=False,
        cumulative=True,
        element="step",
        fill=False,
        hue="EC value",
        kde=True,
        log_scale=True,
        stat="percent",
    )
    plt.title("Percent Error in the Presence of 5-score + 5% Noise")
    uniq_str = str(int(time() * 1000) % 1_620_000_000_000)
    log_dir = f'{get_config_setting("log_dir")}/simulator'
    plt.savefig(f"{log_dir}/ec-noise_{uniq_str}.png")
    plt.clf()
