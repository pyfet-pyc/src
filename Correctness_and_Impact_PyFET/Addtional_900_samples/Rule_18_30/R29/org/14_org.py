def start_scrapping_logic(self):
    page_number = 1
    service_count = 1

    total_url = "https://www.justdial.com/{0}/{1}".format(self.location, self.query)

    fields = ["Name", "Phone", "Rating", "Rating Count", "Address", "Location"]
    out_file = open("{0}.csv".format(self.file_name), "w")
    csvwriter = csv.DictWriter(out_file, delimiter=",", fieldnames=fields)
    csvwriter.writerow(
        {
            "Name": "Name",  # Shows the name
            "Phone": "Phone",  # shows the phone
            "Rating": "Rating",  # shows the ratings
            "Rating Count": "Rating Count",  # Shows the stars for ex: 4 stars
            "Address": "Address",  # Shows the address of the place
            "Location": "Location",  # shows the location
        }
    )

    progress_value = 0
    while True:
        # Check if reached end of result
        if page_number > 50:
            progress_value = 100
            self.progressbar["value"] = progress_value
            break

        if progress_value != 0:
            progress_value += 1
            self.label_progress["text"] = "{0}{1}".format(progress_value, "%")
            self.progressbar["value"] = progress_value

        url = total_url + "/page-%s" % page_number
        print("{0} {1}, {2}".format("Scrapping page number: ", page_number, url))
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
        )
        page = urllib.request.urlopen(req)

        soup = BeautifulSoup(page.read(), "html.parser")
        services = soup.find_all("li", {"class": "cntanr"})

        # Iterate through the 10 results in the page

        progress_value += 1
        self.label_progress["text"] = "{0}{1}".format(progress_value, "%")
        self.progressbar["value"] = progress_value

        for service_html in services:
            try:
                # Parse HTML to fetch data
                dict_service = {}
                name = self.get_name(service_html)
                print(name)
                phone = self.get_phone_number(service_html)
                rating = self.get_rating(service_html)
                count = self.get_rating_count(service_html)
                address = self.get_address(service_html)
                location = self.get_location(service_html)
                if name is not None:
                    dict_service["Name"] = name
                if phone is not None:
                    print("getting phone number")
                    dict_service["Phone"] = phone
                if rating is not None:
                    dict_service["Rating"] = rating
                if count is not None:
                    dict_service["Rating Count"] = count
                if address is not None:
                    dict_service["Address"] = address
                if location is not None:
                    dict_service["Address"] = location

                # Write row to CSV
                csvwriter.writerow(dict_service)

                print("#" + str(service_count) + " ", dict_service)
                service_count += 1
            except AttributeError:
                print("AttributeError Occurred 101")

        page_number += 1

    out_file.close()