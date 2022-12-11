# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/diff_shades_gha_helper.py
# Compiled at: 2022-08-13 03:28:53
# Size of source mod 2**32: 1852 bytes


def config(event: Literal[('push', 'pull_request')]) -> None:
    import diff_shades
    if event == 'push':
        jobs = [
         {'mode':'preview-changes', 
          'force-flag':'--force-preview-style'}]
        baseline_name = str(get_pypi_version())
        baseline_cmd = f"git checkout {baseline_name}"
        target_rev = os.getenv('GITHUB_SHA')
        if target_rev is not None:
            target_name = 'main-' + target_rev[:SHA_LENGTH]
            target_cmd = f"git checkout {target_rev}"
    elif event == 'pull_request':
        jobs = [{'mode':'preview-changes',  'force-flag':'--force-preview-style'},
         {'mode':'assert-no-changes', 
          'force-flag':'--force-stable-style'}]
        baseline_rev = get_main_revision()
        baseline_name = 'main-' + baseline_rev[:SHA_LENGTH]
        baseline_cmd = f"git checkout {baseline_rev}"
        pr_ref = os.getenv('GITHUB_REF')
        pr_num = int(pr_ref[10:-6])
        pr_rev = get_pr_revision(pr_num)
        target_name = f"pr-{pr_num}-{pr_rev[:SHA_LENGTH]}"
        target_cmd = f"gh pr checkout {pr_num} && git merge origin/main"
    env = f"{platform.system()}-{platform.python_version()}-{diff_shades.__version__}"
    for entry in jobs:
        entry['baseline-analysis'] = f"{entry['mode']}-{baseline_name}.json"
        entry['baseline-setup-cmd'] = baseline_cmd
        entry['target-analysis'] = f"{entry['mode']}-{target_name}.json"
        entry['target-setup-cmd'] = target_cmd
        entry['baseline-cache-key'] = f"{env}-{baseline_name}-{entry['mode']}"
        if event == 'pull_request':
            entry['baseline-sha'] = baseline_rev
            entry['target-sha'] = pr_rev
# okay decompiling testbed_py/diff_shades_gha_helper.py
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/final.py
# Compiled at: 2022-08-13 03:28:55
pass
# okay decompiling testbed_py/final.py
# decompiled 2 files: 2 okay, 0 failed
