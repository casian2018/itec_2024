<template>
    <div class="dashboard">
      <nav class="navbar">
        <h1 class="navbar-title">Dashboard</h1>
      </nav>
      <div class="endpoint-list">
        <div v-for="endpoint in endpointuri" :key="endpoint.id" class="endpoint-item grid grid-cols-3">
          <p class="endpoint-url">Website: {{ endpoint.url }}</p>
          <p class="endpoint-status">Status: {{ endpoint.status }}</p>
          <div class="w-full bg-gray-200 rounded">
            <div
              :class="`bg-${color}-500 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded`"
              :style="{ width: `${statusWidth}%` }"
            >{{ statusWidth }}%</div>
          </div>
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
  import { getFirestore, collection, getDocs } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
  
  const firebaseConfig = {
    apiKey: "AIzaSyDTXWIiULSBECNDYj8D6U3pio0TTjyNuCc",
    authDomain: "itec2024.firebaseapp.com",
    projectId: "itec2024",
    storageBucket: "itec2024.appspot.com",
    messagingSenderId: "654897749335",
    appId: "1:654897749335:web:86ad18e39b11b730a1b212",
    measurementId: "G-V38WHRYJ7R"
  };
  
  export default {
    data() {
      return {
        endpointuri: []
      };
    },
    async mounted() {
      const app = initializeApp(firebaseConfig);
      const db = getFirestore(app);
      
      // Function to fetch endpoint data
      const fetchEndpoints = async () => {
        try {
          const endpointsSnapshot = await getDocs(collection(db, 'endpointuri'));
          const updatedEndpoints = [];
  
          endpointsSnapshot.forEach((doc) => {
            updatedEndpoints.push({ id: doc.id, ...doc.data() });
          });
  
          this.endpointuri = updatedEndpoints;
        } catch (error) {
          console.error("Error fetching endpoints:", error);
        }
      };
  
      // Initial fetch
      fetchEndpoints();
  
      // Refresh endpoint data every second
      setInterval(fetchEndpoints, 1);
    }
  };
  </script>
  