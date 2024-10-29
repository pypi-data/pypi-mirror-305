# %%
import sys
sys.path.append('..')

from equitorch.utils.indices import expand_right, expand_left

import torch
import math

device = 'cuda:0'
# device='cpu'
dtype = torch.float64

# _Jd = torch.load(os.path.join(os.path.dirname('/home/wangtong/equitorch/equitorch/equitorch/math/'), "Jd.pt"))


# %%
print(1)

# %%
# # Borrowed from e3nn @ 0.4.0:
# # https://github.com/e3nn/e3nn/blob/0.4.0/e3nn/o3/_wigner.py#L37
# #
# # In 0.5.0, e3nn shifted to torch.matrix_exp which is significantly slower:
# # https://github.com/e3nn/e3nn/blob/0.5.0/e3nn/o3/_wigner.py#L92
# def wigner_D(l, alpha, beta, gamma):
#     if not l < len(_Jd):
#         raise NotImplementedError(
#             f"wigner D maximum l implemented is {len(_Jd) - 1}, send us an email to ask for more"
#         )

#     alpha, beta, gamma = torch.broadcast_tensors(alpha, beta, gamma)
#     J = _Jd[l].to(dtype=alpha.dtype, device=alpha.device)
#     Xa = _z_rot_mat(alpha, l)
#     Xb = _z_rot_mat(beta, l)
#     Xc = _z_rot_mat(gamma, l)
#     return Xa @ J @ Xb @ J @ Xc


# def _z_rot_mat(angle, l):
#     shape, device, dtype = angle.shape, angle.device, angle.dtype
#     M = angle.new_zeros((*shape, 2 * l + 1, 2 * l + 1))
#     inds = torch.arange(0, 2 * l + 1, 1, device=device)
#     reversed_inds = torch.arange(2 * l, -1, -1, device=device)
#     frequencies = torch.arange(l, -l - 1, -1, dtype=dtype, device=device)
#     M[..., inds, reversed_inds] = torch.sin(frequencies * angle[..., None])
#     M[..., inds, inds] = torch.cos(frequencies * angle[..., None])
#     return M

# %%

# import equitorch.utils

# N = 100000

# a,b,c = equitorch.utils.rand_rotation_angles(N, device=device, dtype=dtype)
# l = 11
# D_1 = equitorch.math.so3._wigner_D(l ,a, b, c)
# D_2 = wigner_D(l, a, b, c)
# print((D_1-D_2).abs().max())

# %%
# %timeit -r 5 -n 200 equitorch.math.so3._wigner_D(l ,a, b, c) 
# %timeit -r 5 -n 200 wigner_D(l ,a, b, c) 

# %%
from equitorch.utils import check_degree_range, num_orders_in
from equitorch.typing import DegreeRange

def wigner_D_ptr_ind(L: DegreeRange, device=None):

    l_min, l_max = check_degree_range(L)

    ind = sum((list(range(l**2-l_min**2, (l+1)**2-l_min**2)) * (2*l+1) for l in range(l_min, l_max+1)), [])
    ind = torch.tensor(ind, device=device)

    ptr = sum((list(range((4*l**3-l)//3+2*l+1-(4*l_min**3-l_min)//3, 
                          (4*l**3-l)//3-(4*l_min**3-l_min)//3+(2*l+1)**2+1, 2*l+1)) for l in range(l_min, l_max+1)), [0])
    ptr = torch.tensor(ptr, device=device)

    return ptr, ind

L = (2,3)

ind, ptr = wigner_D_ptr_ind(L)
print(ind)
print(ptr)
val = torch.arange(ind.shape[0])+1
A = torch.sparse_csr_tensor(ptr, ind, val, size=(num_orders_in(L), num_orders_in(L)))
print(A)
# print(A.to_dense())
print(1)
# %%
import torch_geometric
from torch_geometric.utils import segment
import torch_scatter
from equitorch.utils import degrees_in_range

def batch_csr_mul(vec: torch.Tensor, val: torch.Tensor, ptr: torch.Tensor, ind: torch.Tensor, dim=-1):
    vec = vec.index_select(dim, ind)
    elems = expand_right(val,1,0) * vec
    return segment(elems, expand_left(ptr,1,0))

def sparse_wigner_D(L: DegreeRange, a, b, c):
    return (
        torch.cat([equitorch.math.so3._wigner_D(l ,a, b, c).flatten(-2,-1) for l in degrees_in_range(L)], dim=-1),
        wigner_D_ptr_ind(L, a.device)
        )

# %%
import equitorch.math
import equitorch.utils

N = 10000
C = 3
L = (1,2)
a, b, c = equitorch.utils.rand_rotation_angles(N, device=device, dtype=dtype)

Dd = equitorch.math.so3.wigner_D(L, a, b, c)
Ds = sparse_wigner_D(L, a, b, c)

X = torch.randn(N, num_orders_in(L), C, device=device, dtype=dtype)

# %%
DdX = Dd @ X
DsX = batch_csr_mul(X, Ds[0], *(Ds[1]), dim=-2)


# %%
print(DdX.allclose(DsX))
print(DdX.abs().max())
print((DdX-DsX).abs().max())
print(1)



