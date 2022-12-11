def marshall_images(
    coordinates: str,
    image: ImageOrImageList,
    caption: Optional[Union[str, "npt.NDArray[Any]", List[str]]],
    width: int,
    proto_imgs: ImageListProto,
    clamp: bool,
    channels: Channels = "RGB",
    output_format: OutputFormat = "auto",
) -> None:
    channels = cast(Channels, channels.upper())

    # Turn single image and caption into one element list.
    images: Sequence[AtomicImage]
    if isinstance(image, list):
        images = image
    elif isinstance(image, np.ndarray) and len(image.shape) == 4:
        images = _4d_to_list_3d(image)
    else:
        images = [image]

    if type(caption) is list:
        captions: Sequence[Optional[str]] = caption
    else:
        if isinstance(caption, str):
            captions = [caption]
        # You can pass in a 1-D Numpy array as captions.
        elif isinstance(caption, np.ndarray) and len(caption.shape) == 1:
            captions = caption.tolist()
        # If there are no captions then make the captions list the same size
        # as the images list.
        elif caption is None:
            captions = [None] * len(images)
        else:
            captions = [str(caption)]

    assert type(captions) == list, "If image is a list then caption should be as well"
    assert len(captions) == len(images), "Cannot pair %d captions with %d images." % (
        len(captions),
        len(images),
    )

    proto_imgs.width = width
    # Each image in an image list needs to be kept track of at its own coordinates.
    for coord_suffix, (image, caption) in enumerate(zip(images, captions)):
        proto_img = proto_imgs.imgs.add()
        if caption is not None:
            proto_img.caption = str(caption)

        # We use the index of the image in the input image list to identify this image inside
        # InMemoryFileManager. For this, we just add the index to the image's "coordinates".
        image_id = "%s-%i" % (coordinates, coord_suffix)

        is_svg = False
        if isinstance(image, str):
            # Unpack local SVG image file to an SVG string
            if image.endswith(".svg") and not image.startswith(("http://", "https://")):
                with open(image) as textfile:
                    image = textfile.read()

            # Following regex allows svg image files to start either via a "<?xml...>" tag eventually followed by a "<svg...>" tag or directly starting with a "<svg>" tag
            if re.search(r"(^\s?(<\?xml[\s\S]*<svg\s)|^\s?<svg\s)", image):
                proto_img.markup = f"data:image/svg+xml,{image}"
                is_svg = True
        if not is_svg:
            proto_img.url = image_to_url(
                image, width, clamp, channels, output_format, image_id
            )
