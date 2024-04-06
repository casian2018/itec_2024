<template>
    <div class="dashboard">
      <nav class="navbar">
        <h1 class="navbar-title">Dashboard</h1>
      </nav>
      <div class="endpoint-list">
        <div v-for="endpoint in endpointuri" :key="endpoint.id" class="endpoint-item">
          <p class="endpoint-url">URL: {{ endpoint.url }}</p>
          <p class="endpoint-status">Stare: {{ endpoint.stare }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .dashboard {
    padding: 20px;
  }
  
  .navbar {
    background-color: #2196F3;
    color: #fff;
    padding: 10px 20px;
  }
  
  .navbar-title {
    margin: 0;
  }
  
  .endpoint-list {
    margin-top: 20px;
  }
  
  .endpoint-item {
    background-color: #f4f4f4;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .endpoint-url {
    margin: 0;
  }
  
  .endpoint-status {
    margin: 5px 0;
  }
  </style>
  

<script>

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
import { getFirestore, collection, getDocs, updateDoc, doc } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDTXWIiULSBECNDYj8D6U3pio0TTjyNuCc",
    authDomain: "itec2024.firebaseapp.com",
    projectId: "itec2024",
    storageBucket: "itec2024.appspot.com",
    messagingSenderId: "654897749335",
    appId: "1:654897749335:web:86ad18e39b11b730a1b212",
    measurementId: "G-V38WHRYJ7R"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Function to update the status of an endpoint in Firestore
async function updateEndpointStatus(endpointId, newStatus) {
    const endpointRef = doc(db, 'endpointuri', endpointId);
    await updateDoc(endpointRef, {
        status: newStatus
    });
}

export default {
    data() {
        return {
            endpointuri: []
        };
    },
    async mounted() {
        try {
            const endpointsSnapshot = await getDocs(collection(db, 'endpointuri'));
            const updatedEndpoints = [];

            endpointsSnapshot.forEach((doc) => {
                // Call the endpoint and get the status
                // Implement the code to call the endpoint and get the status

                // Assuming newStatus represents the obtained status
                const newStatus = "Stable"; // Example of the obtained status

                // Update the endpoint status in Firebase
                updateEndpointStatus(doc.id, newStatus);
                updatedEndpoints.push({ id: doc.id, ...doc.data(), status: newStatus });
            });

            this.endpointuri = updatedEndpoints;
        } catch (error) {
            console.error("Error fetching endpoints:", error);
        }
    }
};


</script>