def draw_debug_img(args):

    html_path = args.save_html_path

    err_cnt = 0
    f =  open(html_path, 'w')
    
    html.write('<html>\n<body>\n')
    html.write('<table border="1">\n')
    html.write(
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />"
    )
    image_list = []
    path = args.image_dir
    for i, filename in enumerate(sorted(os.listdir(path))):
        if filename.endswith("txt"): continue
        # The image path
        base = "{}/{}".format(path, filename)
        html.write("<tr>\n")
        html.write(f'<td> {filename}\n GT')
        html.write(f'<td>GT\n<img src="{base}" width={args.width}></td>')

        html.write("</tr>\n")
    html.write('<style>\n')
    html.write('span {\n')
    html.write('    color: red;\n')
    html.write('}\n')
    html.write('</style>\n')
    html.write('</table>\n')
    html.write('</html>\n</body>\n')
    print(f"The html file saved in {html_path}")
    return