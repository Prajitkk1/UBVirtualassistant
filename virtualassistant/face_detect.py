import face_recognition
from sklearn import svm
import os
def train_images():
    encodings = []
    names = []
    train_dir = os.listdir('Images/')
    for person in train_dir:
        pix = os.listdir("Images/" + person)

        for person_img in pix:
            face = face_recognition.load_image_file("Images/" + person + "/" + person_img)
            face_bounding_boxes = face_recognition.face_locations(face)
            if len(face_bounding_boxes) == 1:
                face_enc = face_recognition.face_encodings(face)[0]
                encodings.append(face_enc)
                names.append(person)
            else:
                print(person + "/" + person_img + " was skipped and can't be used for training")

    clf = svm.SVC(gamma='scale')

    clf.fit(encodings,names)
    print("i am able to fit it")
    return clf
















