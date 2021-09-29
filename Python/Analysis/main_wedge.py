#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import Wedges.post_labor as post_labor
import Wedges.post_cap as post_cap
import Wedges.post_dynamic as post_dynamic
import Wedges.pre_labor as pre_labor
import Wedges.pre_cap as pre_cap
import Wedges.pre_dynamic as pre_dynamic

# Address of the folder to save the data
output_folder_post = '../../Data/Analysis/Post/'
output_folder_pre = '../../Data/Analysis/Pre/'

# Address of the folder of saved files
input_folder_post = '../../Data/Downloads/Post/'
input_folder_pre = '../../Data/Downloads/Pre/'

# Address of the folder of results
results_folder = '../../Data/Results/'


def main():
    post_labor.main(output_folder_post, results_folder)
    post_cap.main(output_folder_post, results_folder)
    post_dynamic.main(output_folder_post, results_folder)
    pre_labor.main(output_folder_pre, results_folder)
    pre_cap.main(output_folder_pre, results_folder)
    pre_dynamic.main(output_folder_pre, results_folder)


if __name__ == '__main__':
    main()
