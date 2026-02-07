
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.5.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.5.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "XXXXXXXXXXXXXX",
    authDomain: "XXXXXX",
    projectId: "blindassistance-96f93",
    storageBucket: "blindassistance-96f93.firebasestorage.app",
    messagingSenderId: "608637949815",
    appId: "1:608637949815:web:03346206b90b5d9cba7372",
    measurementId: "G-S1DP6L58J7"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
