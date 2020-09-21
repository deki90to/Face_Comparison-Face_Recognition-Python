import face_recognition

image_of_actor = face_recognition.load_image_file('./pictures/known/Richard.png')
actor_face_encoding = face_recognition.face_encodings(image_of_actor)[0]


unknown_image = face_recognition.load_image_file('./pictures/unknown/richard123.png')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]


results = face_recognition.compare_faces([actor_face_encoding], unknown_face_encoding)


if results[0]:
	print('It is Richard.')
else:
	print('Not Richard.')