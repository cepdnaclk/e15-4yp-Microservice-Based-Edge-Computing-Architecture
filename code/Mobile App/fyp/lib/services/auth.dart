import 'package:firebase_auth/firebase_auth.dart';

class AuthService {

  FirebaseAuth auth = FirebaseAuth.instance;

  //anon
  Future signInAnon() async {
    try {
      UserCredential userCredential =
          await auth.signInAnonymously();
      return userCredential;
    } catch (e) {
      print('error in sign in');
      return null;
    }
  }
}
