import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

class Profile extends StatefulWidget {
  @override
  _ProfileState createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  // FirebaseFirestore firestore = FirebaseFirestore.instance;
  bool _initialized = false;
  bool _error = false;

  // Define an async function to initialize FlutterFire
  void initializeFlutterFire() async {
    try {
      // Wait for Firebase to initialize and set `_initialized` state to true
      await Firebase.initializeApp();
      setState(() {
        _initialized = true;
      });
    } catch (e) {
      // Set `_error` state to true if Firebase initialization fails
      setState(() {
        _error = true;
      });
    }
  }

  @override
  void initState() {
    initializeFlutterFire();
    super.initState();
  }

  TextEditingController firstNameController = TextEditingController();
  TextEditingController lastNameController = TextEditingController();
  TextEditingController mobileNumberController = TextEditingController();
  TextEditingController homeAddressController = TextEditingController();

  Future<void> addProfile() {
    CollectionReference profile =
        FirebaseFirestore.instance.collection('profiles');
    // Call the user's CollectionReference to add a new user
    profile.add({
      'first_name': firstNameController.text,
      'last_name': lastNameController.text,
      'mobile_number': mobileNumberController.text,
      'home_address': homeAddressController.text
    }).then((value) {
      print("Profile Added");
      Navigator.pushNamed(context, '/home');
    }).catchError((error) => print("Failed to add Profile: $error"));
  }

  @override
  Widget build(BuildContext context) {
    // Show error message if initialization failed
    if (_error) {
      return Container();
    }

    // Show a loader until FlutterFire is initialized
    if (!_initialized) {
      return Container();
    }

    // Show error message if initialization failed
    return Scaffold(
        appBar: AppBar(
          title: Text('FYP'),
          actions: [
            Icon(Icons.favorite),
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 16),
              child: Icon(Icons.search),
            ),
            Icon(Icons.more_vert),
          ],
          backgroundColor: Colors.grey,
        ),
        drawer: Drawer(
          child: ListView(
            // Important: Remove any padding from the ListView.
            padding: EdgeInsets.zero,
            children: <Widget>[
              DrawerHeader(
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Text('Drawer Header'),
                    // Icon(Icons.menu)
                  ],
                ),
                decoration: BoxDecoration(
                  color: Colors.cyan,
                ),
              ),
              ListTile(
                dense: true,
                title: Row(
                  children: [
                    Icon(Icons.home),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        'Home',
                        textScaleFactor: 1.2,
                      ),
                    ),
                  ],
                ),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pushNamed(context, '/home');
                },
              ),
              ListTile(
                dense: true,
                title: Row(
                  children: [
                    Icon(Icons.account_box),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        'Profile',
                        textScaleFactor: 1.2,
                      ),
                    ),
                  ],
                ),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pushNamed(context, '/profile');
                },
              ),
              ListTile(
                dense: true,
                title: Row(
                  children: [
                    Icon(Icons.airport_shuttle),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        'Vehicles',
                        textScaleFactor: 1.2,
                      ),
                    ),
                  ],
                ),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pushNamed(context, '/vehicle');
                },
              ),
              ListTile(
                dense: true,
                title: Row(
                  children: [
                    Icon(Icons.chat_outlined),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        'Summary',
                        textScaleFactor: 1.2,
                      ),
                    ),
                  ],
                ),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pop(context);
                },
              ),
              ListTile(
                title: SizedBox(height: 10),
              ),
              ListTile(
                dense: true,
                subtitle: Row(
                  children: [
                    // Icon(Icons.chat_outlined),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        'About Us',
                        textScaleFactor: 1.3,
                      ),
                    ),
                  ],
                ),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pop(context);
                },
              ),
              ListTile(
                dense: true,
                subtitle: Row(
                  children: [
                    // Icon(Icons.chat_outlined),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        'Log Out',
                        textScaleFactor: 1.3,
                      ),
                    ),
                  ],
                ),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pop(context);
                },
              ),
            ],
          ),
        ),
        body: Padding(
            padding: EdgeInsets.all(10),
            child: ListView(
              children: <Widget>[
                Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    child: Text(
                      'Add Profile',
                      style: TextStyle(fontSize: 20),
                    )),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: firstNameController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'First Name',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
                  child: TextField(
                    controller: lastNameController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Last Name',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: mobileNumberController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Mobile Number',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: homeAddressController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Home Address',
                    ),
                  ),
                ),
                const SizedBox(height: 30),
                Container(
                    height: 50,
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 0),
                    child: RaisedButton(
                      textColor: Colors.white,
                      color: Colors.blue,
                      child: Text('Register'),
                      onPressed: () async {
                        print(firstNameController.text);
                        print(lastNameController.text);
                        print(mobileNumberController.text);
                        print(homeAddressController.text);
                        addProfile();
                      },
                    )),
              ],
            )));
  }
}
