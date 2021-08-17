def load_image(image):
    [rows, cols, _] = image.shape
    X = image[0:rows, 0:cols//2]
    mask = image[0:rows, cols//2:cols]

    return X, mask

def bin_mask(mask):    # basically setting a range of image
  bins = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 240])
  new_mask = np.digitize(mask, bins)

  return new_mask

def get_Segmented_arr(image, classes, width= WIDTH,height= HEIGHT):
  seg_arr = np.zeros((height, width, classes))
  img = image[:, :, 0]

  for clas in range(classes):
    seg_arr[:, :, clas] = (img == clas).astype(int)

  return seg_arr

def give_color(seg, classes = CLASSES):

  seg_img = np.zeros(seg.shape[0], seg.shape[1], 3)
  colors = sns.color_palette("husl", 13)

  for clas in range(classes):
    seg_c = (seg == clas)
    seg_img[:, :, 0] = (seg_c*(colors[clas][0]))
    seg_img[:, :, 1] = (seg_c*(colors[clas][1]))
    seg_img[:, :, 2] = (seg_c*(colors[clas][2]))

  return (seg_img)

