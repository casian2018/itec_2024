// nuxt.config.js
export default {
  // Alte configurații
  modules: ["@nuxtjs/tailwindcss"],
  buildModules: [
    '@nuxtjs/firebase'
  ],
  firebase: {
    config: {
      apiKey: "AIzaSyDTXWIiULSBECNDYj8D6U3pio0TTjyNuCc",
      authDomain: "itec2024.firebaseapp.com",
      databaseURL: "https://itec2024-default-rtdb.europe-west1.firebasedatabase.app",
      projectId: "itec2024",
      storageBucket: "itec2024.appspot.com",
      messagingSenderId: "654897749335",
      appId: "1:654897749335:web:86ad18e39b11b730a1b212",
      measurementId: "G-V38WHRYJ7R"
    },
    services: {
      firestore: true // Enable Firestore service
    }
  }
}
