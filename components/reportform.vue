<template>
    <nav class=" bg-white w-full flex relative justify-between items-center mx-auto px-8 h-20">
    <div class="inline-flex">
       <img src="/public/logo.png" class="w-44">
    </div>

    <div class="flex-initial">
      <div class="flex justify-end items-center relative">
       
        <div class="flex mr-4 items-center">
          <NuxtLink to="login" class="inline-block py-2 px-3  rounded-full" >
            <div class="flex items-center relative cursor-pointer whitespace-nowrap">Log in</div>
          </NuxtLink>
         
        </div>

        <div class="block">
            <div class="inline relative">
                <div class="flex items-center relative cursor-pointer whitespace-nowrap ">About</div>
            </div>
        </div>
      </div>
    </div>

</nav>


<div class="pt-4 text-2xl"><span class="font-"><center>Professional Website</center><div><span class="text-red-600"><center>Monitoring</center></span></div></span></div>
 
 
      <div class="h-full ml-14 mb-10 md:ml-64 text-black pt-14 pl-24 pr-72 mr-20 ">

        <div class=" flex-col min-w-0 mb-4 lg:mb-0 break-words mx-12 bg-gray-200 mt-4 ">
        
          <div class="dashboard mx-4">
            <main v-if="endpointuri && endpointuri.length">
             
            </main>
            <main v-else>
              <p>No endpoint data available.</p>
            </main>
          </div>

          <div class="flex flex-col mt-4 py-6 px-4">
            <label for="project" class="text-sm font-medium text-gray-900 ">Select Website:</label>
            <select v-model="selectedProject" id="project" name="project" class="form-select mt-1 block w-full border-gray-300 rounded-md shadow-sm p-0.5">
              <option value="" disabled>-</option>
              <option v-for="project in projects" :key="project" :value="project">{{ project }}</option>
            </select>
          
          <input v-model="newBugTitle" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-full mt-4 p-1.5" placeholder="Title">
          <input v-model="newBugDescription" type="text" class="form-input rounded-md shadow-sm border-gray-300 block w-full mt-4 p-1 pb-16" placeholder="Description">
        </div>
          <button @click="addNewBug" class="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 mt-4  w-full">
            REPORT
          </button>
        </div>
        <div class="pt-4 ml-20 text-gray-500 hover:text-gray-700"><NuxtLink to="publicuser"><span>Return</span></NuxtLink></div>
      </div>

      <div class="overflow-x-auto sm:mx-0.5 lg:mx-0.5">
        

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
  const db = getFirestore(app); 
  const states = {
    STABLE: "Stable",
    UNSTABLE: "Unstable",
    DOWN: "Down",
  };
  
  export default {
    data() {
      return {
        endpointuri: [],
        newBugTitle: "",
        newBugDescription: "",
        name: "",
        projects: [], 
        selectedProject: "", 
        bugs: [], 
      };
    },
    async mounted() {
      await this.fetchData(); 
      await this.getUser(); 
  
     
      setInterval(async () => {
        await this.fetchData();
      }, 10000);
    },
    methods: {
      async fetchData() {
        try {
          const endpointsSnapshot = await getDocs(collection(db, "endpointuri"));
          const updatedEndpoints = [];
          const projectURLs = []; 
          endpointsSnapshot.forEach((doc) => {
            updatedEndpoints.push({
              id: doc.id,
              ...doc.data(),
            });
            projectURLs.push(doc.data().url); 
          });
          this.endpointuri = updatedEndpoints;
          this.projects = projectURLs; 
  
        
          const bugsSnapshot = await getDocs(collection(db, "bugs"));
          const bugs = [];
          bugsSnapshot.forEach((doc) => {
            bugs.push({
              id: doc.id,
              ...doc.data(),
            });
          });
          this.bugs = bugs; 
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      },
      async addNewBug() {
        try {
          const title = this.newBugTitle.trim();
          const description = this.newBugDescription.trim();
          if (title && description && this.selectedProject) {
           
            await addDoc(collection(db, "bugs"), { title, description, project: this.selectedProject }); 
            this.newBugTitle = "";
            this.newBugDescription = "";
          }
        } catch (error) {
          console.error("Error adding new bug:", error);
        }
      },
      async getUser() {
        try {
          const userData = await getDocs(collection(db, "users"));
          const userDoc = userData.docs[0];
          this.name = userDoc.data().Name;
        } catch (error) {
          console.error("Error fetching user data:", error);
        }
      },
      getStatusWidth(status) {
        switch (status) {
          case states.STABLE:
            return '100%'; 
          case states.UNSTABLE:
            return '50%'; 
          case states.DOWN:
            return '30%'; 
          default:
            return '0%'; 
        }
      },
      filteredBugs(endpointURL) {
        if (endpointURL) {
          return this.bugs.filter(bug => bug.project === endpointURL);
        } else {
          return this.bugs;
        }
      }
    },
  };
  </script>
  




  