import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

class AddVehicle extends StatefulWidget {
  @override
  _AddVehicleState createState() => _AddVehicleState();
}

class _AddVehicleState extends State<AddVehicle> {
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

  TextEditingController brandController = TextEditingController();
  TextEditingController modelController = TextEditingController();
  TextEditingController manufacturerController = TextEditingController();
  TextEditingController numberPlateController = TextEditingController();

  Future<void> addVehicle() {
    CollectionReference profile =
        FirebaseFirestore.instance.collection('vehicles');
    // Call the user's CollectionReference to add a new user
    profile
        .add({
          'brand': brandController.text,
          'model': modelController.text,
          'manufacturer': manufacturerController.text,
          'number_plate': numberPlateController.text
        })
        .then((value)  {
          print("Vehicle Added");
          Navigator.pushNamed(context, '/home');
        })
        .catchError((error) => print("Failed to add Vehicle: $error"));
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
                      'Add Vehicle',
                      style: TextStyle(fontSize: 20),
                    )),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: brandController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Brand',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
                  child: TextField(
                    controller: modelController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Model',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: manufacturerController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Manufacturer',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: numberPlateController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Number Plate',
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
                        print(brandController.text);
                        print(modelController.text);
                        print(manufacturerController.text);
                        print(numberPlateController.text);
                        addVehicle();
                      },
                    )),
              ],
            )));
  }
}
