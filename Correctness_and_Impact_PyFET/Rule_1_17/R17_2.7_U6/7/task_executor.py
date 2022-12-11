
def _get_loop_items(self):
    '''
    Loads a lookup plugin to handle the with_* portion of a task (if specified),
    and returns the items result.
    '''

    # get search path for this task to pass to lookup plugins
    self._job_vars['ansible_search_path'] = self._task.get_search_path()

    # ensure basedir is always in (dwim already searches here but we need to display it)
    if self._loader.get_basedir() not in self._job_vars['ansible_search_path']:
        self._job_vars['ansible_search_path'].append(self._loader.get_basedir())

    templar = Templar(loader=self._loader, variables=self._job_vars)
    items = None
    loop_cache = self._job_vars.get('_ansible_loop_cache')
    if loop_cache is not None:
        # _ansible_loop_cache may be set in `get_vars` when calculating `delegate_to`
        # to avoid reprocessing the loop
        items = loop_cache
    elif self._task.loop_with:
        if self._task.loop_with in self._shared_loader_obj.lookup_loader:
            fail = True
            if self._task.loop_with == 'first_found':
                # first_found loops are special. If the item is undefined then we want to fall through to the next value rather than failing.
                fail = False

            loop_terms = listify_lookup_plugin_terms(terms=self._task.loop, templar=templar, fail_on_undefined=fail, convert_bare=False)
            if not fail:
                loop_terms = [t for t in loop_terms if not templar.is_template(t)]

            # get lookup
            mylookup = self._shared_loader_obj.lookup_loader.get(self._task.loop_with, loader=self._loader, templar=templar)

            # give lookup task 'context' for subdir (mostly needed for first_found)
            for subdir in ['template', 'var', 'file']:  # TODO: move this to constants?
                if subdir in self._task.action:
                    break
            setattr(mylookup, '_subdir', subdir + 's')

            # run lookup
            items = wrap_var(mylookup.run(terms=loop_terms, variables=self._job_vars, wantlist=True))
        else:
            raise AnsibleError("Unexpected failure in finding the lookup named '%s' in the available lookup plugins" % self._task.loop_with)

    elif self._task.loop is not None:
        items = templar.template(self._task.loop)
        if not isinstance(items, list):
            raise AnsibleError(
                "Invalid data passed to 'loop', it requires a list, got this instead: %s."
                " Hint: If you passed a list/dict of just one element,"
                " try adding wantlist=True to your lookup invocation or use q/query instead of lookup." % items
            )

    return items
