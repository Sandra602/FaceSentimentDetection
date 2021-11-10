import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/adish/OneDrive/Desktop/qwiklabs-gcp-04-4c39ff72a2f8-11f562a2fc07.json"

def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    face_res=[]
    for face in faces:
        face_res.append('Anger: {}'.format(likelihood_name[face.anger_likelihood]))
        face_res.append('Joy: {}'.format(likelihood_name[face.joy_likelihood]))
        face_res.append('Surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    if response.error.message:
        raise Exception(
            '{}/nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return face_res