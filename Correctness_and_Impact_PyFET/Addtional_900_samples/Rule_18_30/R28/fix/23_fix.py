def save(self, *args, **kwargs):
    if self._state.adding and not self.slug:
        self.slug = self.slugify(self.name)

        # if name is different but slug conficts with another tags slug, append a counter
        # with transaction.atomic():
        slugs = set(
            type(self)
            ._default_manager.filter(slug__startswith=self.slug)
            .values_list("slug", flat=True)
        )

        i = None
        while True:
            slug = self.slugify(self.name, i)
            if slug not in slugs:
                self.slug = slug
                return super().save(*args, **kwargs)
            i = 1 if i is None else i+1
    else:
        return super().save(*args, **kwargs)