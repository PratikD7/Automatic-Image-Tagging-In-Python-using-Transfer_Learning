
Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
Search



Gmail
COMPOSE
Labels
Inbox (120)
Starred
Important
Sent Mail
Drafts (30)
Circles
Personal
Travel
Xolo Call History
Xolo SMS
More
Hangouts



  More
1 of 571

Print all In new window
php
Inbox
x

nishant kashiv
Attachments7:09 PM (1 minute ago)

to me
Attachments area

Click here to Reply or Forward
1.99 GB (13%) of 15 GB used
Manage
Terms - Privacy
Last account activity: 3 hours ago
Details
Nishant Kashiv's profile photo
Nishant Kashiv
Friends

Show details


<?php

	if($_SERVER['REQUEST_METHOD']=='POST'){

		$image = $_POST['image'];
                $name = $_POST['name'];
		/*
		require_once('dbConnect.php');

		$sql ="SELECT id FROM volleyupload ORDER BY id ASC";

		$res = mysqli_query($con,$sql);

		$id = 0;

		while($row = mysqli_fetch_array($res)){
				$id = $row['id'];
		}
		*/
		$path = "Pre-Trained/Testing_images/$name.jpeg";

		$actualpath = "http://localhost/VolleyUpload/$path";
		/*
		$sql = "INSERT INTO volleyupload (photo,name) VALUES ('$actualpath','$name')";

		if(mysqli_query($con,$sql)){
		*/
			shell_exec('rm -rf Pre-Trained/Testing_images/*');
			file_put_contents($path,base64_decode($image));
			echo "Successfully Uploaded";
			//$command = escapeshellcmd();
			//$output = system('python2 main4.py');
			//$output = system('python2 p.py');
			//echo $output;
			//ob_start();
			//passthru('python2 main4.py');
			//$output = ob_get_clean();
			#echo $output;
			//echo "Hua run?";
		/*
		}

		mysqli_close($con);
		*/
	}else{
		echo "Error";
	}
upload.php
Open with Drive Notepad
Displaying upload.php.