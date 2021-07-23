## Module 1 Project

### Qwiklabs Assessment: Scale and convert images using PIL

**Introduction**

Your company is in the process of updating its website, and they’ve hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You’re not able to get in contact with the designers and your own deadline is approaching fast. You’ll need to use Python to get these images ready for launch.

**What you'll do**

Use the Python Imaging Library to do the following to a batch of images:

- Open an image
- Rotate an image
- Resize an image
- Save an image in a specific format in a separate directory 

---

#### Solution

Create and run convert_image.py script inside /images directory. Before that, make the script executable. 

```
chmod +x convert_images.py
./convert_images.py
```

Once images have been converted, change directory to /opt/icons/ and check that the converted images exist

```
cd /opt/icons/
ls
```

