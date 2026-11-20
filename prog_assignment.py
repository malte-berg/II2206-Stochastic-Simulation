import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    seed = 333
    return mo, np, seed


@app.cell
def _(np, seed):
    np.random.seed(seed)
    lambd = 3.5
    N = 4
    beta = 0.2
    return (beta,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A call center serves customer phone requests that arrive according to a Poisson process with the rate **λ** (customers/minute). The customers are immediately sent to a free service clerk. Otherwise, the customer is put in a first-come-first-served queue. The arriving customer is informed about the current (short-term) estimate of the time in the queue, ω, which is calculated by taking an average of the waiting time in the queue of the last 10 customers that left the system. If a customer at arrival is informed that the estimated waiting time is ω minutes, the customer leaves the queue with the probability

    p(ω) = Pr[Customer will leave queue if estimated waiting time is ω] = 1-exp(-**β**ω),

    otherwise the customer will wait in the queue. There are **N** service clerks serving customers, and the time to serve a customer is uniformly distributed over [10,110] seconds.

    Write a discrete event simulation in Python (or MATLAB) that will provide a point estimate of the following parameters in minutes

    a) the expected waiting time in the queue,

    b) the expected total time in the system, and

    c) the expected rate of discouraged arrivals ( i.e., how many customers/minute leave the queue without being served)

    The standard deviation of the point estimate should be less than 3 % of the value of the estimate.
    """)
    return


@app.cell
def _(math, np):
    def get_random_service_time():
        return math.floor(np.random.uniform()*101) + 10

    return


@app.cell
def _(beta, math):
    def get_leave_prob(omega):
        return 1 - math.exp(- beta * omega)

    return (get_leave_prob,)


@app.cell
def _(get_leave_prob, np):
    def willing_to_wait(last_ten):
        omega = np.mean(last_ten)
        u = np.random.uniform
        if u < get_leave_prob(omega):
            return True
        return False

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
