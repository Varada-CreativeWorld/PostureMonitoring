# PostureMonitoring

Posture Monitoring model, we have used PoseNet. 
PoseNet provides us with pre-trained models necessary to detect user gestures. These pre-trained models run in our browser and this is what differentiates PoseNet from other API dependent libraries. Hence, we don’t have to send our private data to some backend server. The protection of privacy is what gives PoseNet an edge over other API dependent libraries.

Live webcam feed is taken and passes through PoseNet model. 
PoseNet model returns the coordinates of eyes, nose and ears.
These coordinates are used to get the position of the face and establish boundaries for correct posture.
If the head moves out of the established boundary an alarm sound is played until the head is brought back within the boundary.
The size of the boundary can be adjusted in the settings menu.

PoseNet provides us with pre-trained models necessary to detect user gestures. These pre-trained models run in our browser and this is what differentiates PoseNet from other API dependent libraries. Hence, we don’t have to send our private data to some backend server. The protection of privacy is what gives PoseNet an edge over other API dependent libraries.
PoseNet gives us a total of 17 pose key-points which we can make use of, right from our eyes and ears to our knees and ankles.

Live webcam feed is taken and passes through PoseNet model. More information can be obtained here. Posenet model returns the coordinates of eyes, nose and ears. These coordinates are are used to get the position of the face and establish boundaries for correct posture. If the head moves out of the established boundary an alarm sound is played until the head is brought back within the boundary. The size of the boundary can be adjusted in the settings menu.
