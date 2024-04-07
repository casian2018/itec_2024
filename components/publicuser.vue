
<template>

<nav class=" bg-white w-full flex relative justify-between items-center mx-auto px-8 h-20">
    <div class="inline-flex">
      <img src="/public/logo.png" class="w-44">
    </div>
    <div class="flex-initial">
      <div class="flex justify-end items-center relative">
        <div class="flex mr-4 items-center">
          <NuxtLink to="login" class="inline-block py-2 px-3 rounded-full">
            <div class="flex items-center relative cursor-pointer whitespace-nowrap">Panel</div>
          </NuxtLink>
        </div>
        <div class="block">
          <div class="inline relative">
            <div class="flex items-center relative cursor-pointer whitespace-nowrap">Contact</div>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <div class="pt-4 text-2xl font-lilita-one-regular">
    <center>
      <div>Professional Website</div>
      <div>
        <span class="text-red-600">Monitoring</span>
      </div>
    </center>
  </div>

  <div class="fixed flex-col justify-center">
    
    <div class="flex justify-start bg-white dark:bg-white-500 text-black dark:text-white">
      <div class="h-full ml-14 mb-10 md:ml-64 text-black">
        <!-- Social Traffic -->
        <div class="fixed flex-col justify-center min-w-0 mb-4 lg:mb-0 break-words px-16 mt-2 rounded-xl">
        <div class="dashboard mx-4 ">
            <main v-if="endpointuri && endpointuri.length">
              <div v-for="endpoint in endpointuri" :key="endpoint.id" class="endpoint-item grid grid-cols-3 mt-4">
                <p class="endpoint-url p-1">{{ endpoint.url }}</p>
                <p class="endpoint-status pl-12">
                  Status: {{ endpoint.status }}
                  <span class="ml-2 mr-10 text-xs font-medium rounded-full px-2"></span>
                </p> 
                <div class="w-full rounded">
                  <div :class="`bg-blue-500 text-xs font-medium text-blue-100 text-center p-1 mt-3 leading-none rounded`"
                    :style="{ width: getStatusWidth(endpoint.status) }">
              
                  </div>
                 
                </div>
              
              
              </div>
              
         
            </main>
          
            <main v-else>
              <p>No endpoint data available.</p>
            </main>
         
          </div>
       
          <div class="pt-2">
            <center>
              <NuxtLink to="reportform">
                <button class="border-2 border-red-600 rounded-md bg-red-600 px-4 py-1 text-lg">REPORT</button>
              </NuxtLink>
            </center>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getFirestore, collection, addDoc, getDocs } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";
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

const app = initializeApp(firebaseConfig);
const db = getFirestore(app); // Initialize Firestore
const states = {
  STABLE: "Stable",
  UNSTABLE: "Unstable",
  DOWN: "Down",
};

export default {
  data() {
    return {
      endpointuri: [],
      newEndpointUrl: "",
      name: "",
    };
  },
  async mounted() {
    await this.fetchData(); // Fetch initial data // Fetch user data

    // Refresh data every 10 seconds
    setInterval(async () => {
      await this.fetchData();
    }, 10000);
  },
  methods: {
    async fetchData() {
      try {
        const endpointsSnapshot = await getDocs(collection(db, "endpointuri"));
        const updatedEndpoints = [];
        endpointsSnapshot.forEach((doc) => {
          updatedEndpoints.push({
            id: doc.id,
            ...doc.data(),
          });
        });
        this.endpointuri = updatedEndpoints;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    async addNewEndpoint() {
      try {
        const url = this.newEndpointUrl.trim();
        if (url) {
          await addDoc(collection(db, "endpointuri"), { url, status: "" });
          await this.fetchData(); // Fetch updated data
          this.newEndpointUrl = ""; // Clear input field
        }
      } catch (error) {
        console.error("Error adding new endpoint:", error);
      }
    },

    getStatusWidth(status) {
      switch (status) {
        case states.STABLE:
          return '100%'; // If status is stable, width is 100%
        case states.UNSTABLE:
          return '50%'; // If status is unstable, width is 50%
        case states.DOWN:
          return '30%'; // If status is down, width is 30%
        default:
          return '0%'; // Default width is 0%
      }
    },
  },
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
  color: black;
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
  background-color: #d9d9d9;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 20px;
}

.endpoint-url {
  margin: 0;
}

.endpoint-status {
  margin: 5px 0;
}



</style>
