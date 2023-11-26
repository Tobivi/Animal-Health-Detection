from pygoogle_image import image as pi
# images_to_be_downloaded = ["Unhealthy poultry chicken","healthy poultry chicken","healthy goat","Unhealthy goat","Unhealthy Cow","healthy Cow","Unhealthy sheep","healthy pig","Unhealthy pig"]


with open("datasets.txt",'rb') as data:
    for line in data:
        decoded_line = line.decode('utf-8')


        images = decoded_line.strip()

        pi.download(keywords=images, limit = 100)