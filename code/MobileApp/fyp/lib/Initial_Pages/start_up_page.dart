import 'package:flutter/material.dart';

// ignore: camel_case_types
class Start_Up_Page extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
          image: DecorationImage(
              image: AssetImage("assets/start_up_image.jpg"),
              fit: BoxFit.cover)),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Container(
          margin: EdgeInsets.only(left: 8, top: 300, right: 11.7),
          child: Column(
            children: [
              // Welcome to FYP
              Text("Welcome to FYP",
                  style: const TextStyle(
                      color: Colors.limeAccent,
                      fontWeight: FontWeight.w600,
                      fontFamily: "Gibson",
                      fontStyle: FontStyle.normal,
                      fontSize: 50),
                  textAlign: TextAlign.center),
              // The best way to navigate your world and discover new places. Let's get started!
              Opacity(
                opacity: 0.7830690145492554,
                child: Text(
                    "The best way to navigate your world and discover new places. Let's get started!",
                    style: const TextStyle(
                        color: const Color(0xffffffff),
                        fontWeight: FontWeight.w400,
                        fontFamily: "Gibson",
                        fontStyle: FontStyle.normal,
                        fontSize: 13),
                    textAlign: TextAlign.center),
              ),
              const SizedBox(height: 30),
              RaisedButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/signin');
                },
                textColor: Colors.white,
                padding: const EdgeInsets.all(0.0),
                child: Container(
                  decoration: const BoxDecoration(
                    gradient: LinearGradient(
                      colors: <Color>[
                        Color(0xFF0D47A1),
                        Color(0xFF1976D2),
                        Color(0xFF42A5F5),
                      ],
                    ),
                  ),
                  padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 10),
                  child: const Text('Continue',
                      style: TextStyle(fontSize: 20)),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
