# -*- coding: utf-8 -*-

import os
import jax.numpy as jnp
import econpizza as ep

filepath = os.path.dirname(__file__)


def test_bh(create=False):

    mod = ep.load(ep.examples.bh, raise_errors=False)
    _ = mod.solve_stst()

    state = jnp.zeros(len(mod["variables"]))
    state = state.at[:-1].set([0.1, 0.2, 0.0])

    x, flag = ep.find_path_shooting(
        mod, state, horizon=50, max_horizon=500, tol=1e-8, verbose=2)

    path = os.path.join(filepath, "test_storage", "bh.npy")

    assert flag == 0
    if create:
        jnp.save(path, x)
        print(f'Test file updated at {path}')
    else:
        test_x = jnp.load(path)
        assert jnp.allclose(x, test_x)


def test_nk(create=False):

    mod = ep.load(ep.examples.nk)
    _ = mod.solve_stst()

    state = mod["stst"].copy()
    state["beta"] *= 1.02

    x, flag = ep.find_path_shooting(mod, state.values(), horizon=10,
                                    max_horizon=10, verbose=2)

    path = os.path.join(filepath, "test_storage", "nk.npy")

    assert flag == 0
    if create:
        jnp.save(path, x)
        print(f'Test file updated at {path}')
    else:
        test_x = jnp.load(path)
        assert jnp.allclose(x, test_x)


def test_stacked(create=False):

    mod = ep.load(ep.examples.nk)
    _ = mod.solve_stst()

    shk = ("e_beta", 0.02)

    x, flag = ep.find_path_stacking(mod, shock=shk, horizon=50)

    path = os.path.join(filepath, "test_storage", "stacked.npy")

    assert flag == 0
    if create:
        jnp.save(path, x)
        print(f'Test file updated at {path}')
    else:
        test_x = jnp.load(path)
        assert jnp.allclose(x, test_x)


def test_hank(create=False):

    mod_dict = ep.parse(ep.examples.hank)
    mod = ep.load(mod_dict)
    _ = mod.solve_stst(tol=1e-8)

    x0 = mod['stst'].copy()
    x0['beta'] *= 1.01  # setting a shock on the discount factor

    x, flag = mod.find_path(init_state=x0.values(), horizon=50)
    x_lin, _ = mod.find_path_linear(init_state=x0.values(), horizon=50)
    het_vars = mod.get_distributions(x)
    dist = het_vars['dist']

    path_x = os.path.join(filepath, "test_storage", "hank.npy")
    path_x_lin = os.path.join(filepath, "test_storage", "hank_lin.npy")
    path_dist = os.path.join(filepath, "test_storage", "hank_dist.npy")

    assert flag == 0
    if create:
        jnp.save(path_x, x)
        jnp.save(path_x_lin, x_lin)
        jnp.save(path_dist, dist)
        print(f'Test file updated at {path_x},{path_x_lin} and {path_dist}')
    else:
        test_x = jnp.load(path_x)
        test_x_lin = jnp.load(path_x_lin)
        test_dist = jnp.load(path_dist)
        assert jnp.allclose(x, test_x)
        assert jnp.allclose(x_lin, test_x_lin)
        assert jnp.allclose(dist, test_dist)


def test_hank_labor(create=False):

    mod_dict = ep.parse(ep.examples.hank_labor)
    mod = ep.load(mod_dict)
    _ = mod.solve_stst(tol=1e-8)

    shocks = ('e_beta', .005)

    x, flag = mod.find_path(shocks, horizon=50)

    path = os.path.join(filepath, "test_storage", "hank_labor.npy")

    assert flag == 0
    if create:
        jnp.save(path, x)
        print(f'Test file updated at {path}')
    else:
        test_x = jnp.load(path)
        assert jnp.allclose(x, test_x)


def test_hank2(create=False):

    mod_dict = ep.parse(ep.examples.hank2)
    mod = ep.load(mod_dict)
    _ = mod.solve_stst(tol=1e-6)

    x0 = mod['stst'].copy()
    x0['beta'] *= 1.005  # setting a shock on the discount factor

    x, flag = mod.find_path(init_state=x0.values(), horizon=50)

    path = os.path.join(filepath, "test_storage", "hank2.npy")

    assert flag == 0
    if create:
        jnp.save(path, x)
        print(f'Test file updated at {path}')
    else:
        test_x = jnp.load(path)
        assert jnp.allclose(x, test_x)


def test_solid(create=False):

    mod_dict = ep.parse(ep.examples.hank)
    mod = ep.load(mod_dict)
    _ = mod.solve_stst(tol=1e-8)

    shocks = ('e_beta', .01)

    x, flag = mod.find_path(shocks, use_solid_solver=True,
                            horizon=20, chunk_size=90)

    path = os.path.join(filepath, "test_storage", "hank_solid.npy")

    assert flag == 0
    if create:
        jnp.save(path, x)
        print(f'Test file updated at {path}')
    else:
        test_x = jnp.load(path)
        assert jnp.allclose(x, test_x)


def create_all():

    test_bh(create=True)
    test_nk(create=True)
    test_stacked(create=True)
    test_hank(create=True)
    test_hank_labor(create=True)
    test_hank2(create=True)
    test_solid(create=True)
