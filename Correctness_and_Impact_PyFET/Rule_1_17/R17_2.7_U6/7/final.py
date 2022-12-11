# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/task_executor.py
# Compiled at: 2022-08-11 19:43:39
# Size of source mod 2**32: 2681 bytes


def _get_loop_items(self):
    """
    Loads a lookup plugin to handle the with_* portion of a task (if specified),
    and returns the items result.
    """
    self._job_vars['ansible_search_path'] = self._task.get_search_path()
    if self._loader.get_basedir() not in self._job_vars['ansible_search_path']:
        self._job_vars['ansible_search_path'].append(self._loader.get_basedir())
    templar = Templar(loader=(self._loader), variables=(self._job_vars))
    items = None
    loop_cache = self._job_vars.get('_ansible_loop_cache')
    if loop_cache is not None:
        items = loop_cache
    else:
        if self._task.loop_with:
            if self._task.loop_with in self._shared_loader_obj.lookup_loader:
                fail = True
                if self._task.loop_with == 'first_found':
                    fail = False
                loop_terms = listify_lookup_plugin_terms(terms=(self._task.loop), templar=templar, fail_on_undefined=fail, convert_bare=False)
                if not fail:
                    loop_terms = [t for t in loop_terms if not templar.is_template(t)]
                mylookup = self._shared_loader_obj.lookup_loader.get((self._task.loop_with), loader=(self._loader), templar=templar)
                for subdir in ('template', 'var', 'file'):
                    if subdir in self._task.action:
                        break
                    setattr(mylookup, '_subdir', subdir + 's')
                    items = wrap_var(mylookup.run(terms=loop_terms, variables=(self._job_vars), wantlist=True))

            else:
                raise AnsibleError("Unexpected failure in finding the lookup named '%s' in the available lookup plugins" % self._task.loop_with)
        else:
            if self._task.loop is not None:
                items = templar.template(self._task.loop)
                if not isinstance(items, list):
                    raise AnsibleError("Invalid data passed to 'loop', it requires a list, got this instead: %s. Hint: If you passed a list/dict of just one element, try adding wantlist=True to your lookup invocation or use q/query instead of lookup." % items)
            return items
# okay decompiling testbed_py/task_executor.py
