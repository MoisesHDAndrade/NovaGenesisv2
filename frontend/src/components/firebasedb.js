// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getFirestore} from 'firebase/firestore';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBSxO0PSzhThtnqIOTatbf5rPt77qnO6z8",
  authDomain: "novagenesis-53b6a.firebaseapp.com",
  projectId: "novagenesis-53b6a",
  storageBucket: "novagenesis-53b6a.appspot.com",
  messagingSenderId: "974704252479",
  appId: "1:974704252479:web:8adf0c6977f9e1101c4a8a"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const db =  getFirestore(app);