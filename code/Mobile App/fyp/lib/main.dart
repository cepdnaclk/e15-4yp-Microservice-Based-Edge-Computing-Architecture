import 'package:flutter/material.dart';
import 'package:fyp/Dashboard/Navigation_Bar/Profile.dart';

import 'Dashboard/Home_Page.dart';
import 'Dashboard/Navigation_Bar/Add_Vehicle.dart';
import 'Initial_Pages/sign_in.dart';
import 'Initial_Pages/sign_up.dart';
import 'Initial_Pages/start_up_page.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MaterialApp(
    initialRoute: '/start',
    routes: {
      '/start': (context) => Start_Up_Page(),
      '/home': (context) => Home(),
      '/signin': (context) => SignIn(),
      '/signup': (context) => SignUp(),
      '/profile': (context) => Profile(),
      '/vehicle': (context) => AddVehicle(),
    },
  ));
}

// import 'dart:async';
// import 'dart:convert';
//
// import 'package:flutter/material.dart';
// import 'package:http/http.dart' as http;
//
// Future<Album> fetchAlbum() async {
//   final response =
//   await http.get('http://100.111.129.133:5000/cards');
//
//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     print(response.body);
//     return Album.fromJson(jsonDecode(response.body));
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to load album');
//   }
// }
//
//
// Future<Album> sentAlbum() async {
//   var bodyEncoded = json.encode({'name': 'abacaba'});
//   final response =
//   await http.post(
//       'http://172.17.217.1:3101/add_data',
//       headers: {"Content-Type": "application/json"},
//       body: bodyEncoded
//   );
//
//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     print(response.body);
//     return Album.fromJson(jsonDecode(response.body));
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to load album');
//   }
// }
//
// class Album {
//   final int userId;
//   final int id;
//   final String title;
//
//   Album({this.userId, this.id, this.title});
//
//   factory Album.fromJson(Map<String, dynamic> json) {
//     return Album(
//       userId: json['userId'],
//       id: json['id'],
//       title: json['title'],
//     );
//   }
// }
//
// void main() => runApp(MyApp());
//
// class MyApp extends StatefulWidget {
//   MyApp({Key key}) : super(key: key);
//
//   @override
//   _MyAppState createState() => _MyAppState();
// }
//
// class _MyAppState extends State<MyApp> {
//   Future<Album> _futureAlbum;
//
//   @override
//   void initState() {
//     super.initState();
//     // futureAlbum = fetchAlbum();
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'Fetch Data Example',
//       theme: ThemeData(
//         primarySwatch: Colors.blue,
//       ),
//       home: Scaffold(
//         appBar: AppBar(
//           title: Text('Fetch Data Example'),
//         ),
//         body: Container(
//           alignment: Alignment.center,
//           padding: const EdgeInsets.all(8.0),
//           child: (_futureAlbum == null)
//               ? Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: <Widget>[
//               ElevatedButton(
//                 child: Text('Create Data'),
//                 onPressed: () {
//                   sentAlbum();
//                 },
//               ),
//             ],
//           )
//               : FutureBuilder<Album>(
//             future: _futureAlbum,
//             builder: (context, snapshot) {
//               if (snapshot.hasData) {
//                 return Text(snapshot.data.title);
//               } else if (snapshot.hasError) {
//                 return Text("${snapshot.error}");
//               }
//
//               return CircularProgressIndicator();
//             },
//           ),
//         ),
//       ),
//     );
//   }
// }