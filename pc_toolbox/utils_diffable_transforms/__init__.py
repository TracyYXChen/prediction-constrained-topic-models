from pc_toolbox.utils_diffable_transforms import util_differentiable_transform__2D_rows_sum_to_one \
    as tfm__2D_rows_sum_to_one
from pc_toolbox.utils_diffable_transforms import util_differentiable_transform__unit_interval \
    as tfm__unit_interval
from pc_toolbox.utils_diffable_transforms import util_differentiable_transform__log_unit_interval \
    as tfm__log_unit_interval

# Make a few functions easily available
logistic_sigmoid = tfm__unit_interval.logistic_sigmoid
log_logistic_sigmoid = tfm__log_unit_interval.log_logistic_sigmoid
