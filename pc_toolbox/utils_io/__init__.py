from pc_toolbox.utils_io.pprint_logging import pprint, config_pprint_logging
from pc_toolbox.utils_io.util_pprint_percentiles import make_percentile_str

from pc_toolbox.utils_io.util_watermark import make_string_of_reachable_modules_with_versions

from pc_toolbox.utils_io.util_timing import (
    start_timer_segment,
    stop_timer_segment,
    pprint_timer_segments,
    )

from pc_toolbox.utils_io.util_io_training import (
    do_print_now,
    do_save_now,
    default_settings_alg_io,
    init_alg_state_kwargs,
    update_alg_state_kwargs,
    make_status_string,
    save_status_to_txt_files,
    append_to_txtfile,
    update_alg_state_kwargs_after_print,
    update_alg_state_kwargs_after_save,
    update_symbolic_link,
    calc_laps_when_snapshots_saved,
    )

from pc_toolbox.utils_io.util_setup import (
    setup_detect_taskid_and_insert_into_output_path,
    setup_random_seed,
    setup_output_path,
    write_user_provided_kwargs_to_txt,
    write_env_vars_to_txt,
    write_python_module_versions_to_txt,
    )

from pc_toolbox.utils_io.util_io_csr import (
    load_csr_matrix,
    save_csr_matrix,
    load_csr_matrix_from_ldac_txtfile,
    )

from pc_toolbox.utils_io.util_io_txt import (
    load_list_of_strings_from_txt,
    load_list_of_unicode_from_txt,
    )

from pc_toolbox.utils_io.util_array import (
    toCArray,
    as1D,
    as2D,
    as3D)
