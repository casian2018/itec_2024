<template>
    <!-- component -->
  
  <div>
      <div class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-gray-700 text-black dark:text-white">
  
        <!-- Header -->
        <div class="fixed w-full flex items-center justify-between h-14 text-white z-10">
          <div class="flex items-center justify-start md:justify-center pr-32 w-14 md:w-64 h-14 bg-blue-800 dark:bg-gray-800 border-none">
            <img class="w-7 h-7 md:w-10 md:h-10 mr-2 rounded-md overflow-hidden" src="https://therminic2018.eu/wp-content/uploads/2018/07/dummy-avatar.jpg" />
            <NuxtLink to="login"><span class="hidden md:block hover:text-gray-300 ">Log in</span></NuxtLink>
          </div>
          
        </div>
        <!-- ./Header -->
      
        <!-- Sidebar -->
        <div class="fixed flex flex-col top-14 left-0 w-14 hover:w-64 md:w-64 bg-blue-900 dark:bg-gray-900 h-full text-white transition-all duration-300 border-none z-10 sidebar">
          <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
            <ul class="flex flex-col py-4 space-y-1">
              <li class="px-5 hidden md:block">
                <div class="flex flex-row items-center h-8">
                  <div class="text-sm font-light tracking-wide text-gray-400 uppercase">Main</div>
                </div>
              </li>
              <li>
                <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-800 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                  <span class="inline-flex justify-center items-center ml-4">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                  </span>
                  <span class="ml-2 text-sm tracking-wide truncate">Dashboard</span>
                </a>
              </li>
              <li>
                <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-800 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                  <span class="inline-flex justify-center items-center ml-4">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                  </span>
                  <span class="ml-2 text-sm tracking-wide truncate">Board</span>
                  <span class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-blue-500 bg-indigo-50 rounded-full">New</span>
                </a>
              </li>
              <li>
                <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-800 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                  <span class="inline-flex justify-center items-center ml-4">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg>
                  </span>
                  <span class="ml-2 text-sm tracking-wide truncate">Messages</span>
                </a>
              </li>
              <li>
                <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-800 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                  <span class="inline-flex justify-center items-center ml-4">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
                  </span>
                  <span class="ml-2 text-sm tracking-wide truncate">Notifications</span>
                  <span class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-red-500 bg-red-50 rounded-full">1.2k</span>
                </a>
              </li>
              <li class="px-5 hidden md:block">
                <div class="flex flex-row items-center mt-5 h-8">
                  <div class="text-sm font-light tracking-wide text-gray-400 uppercase">Settings</div>
                </div>
              </li>
              <li>
                <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-800 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                  <span class="inline-flex justify-center items-center ml-4">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                  </span>
                  <span class="ml-2 text-sm tracking-wide truncate">Profile</span>
                </a>
              </li>
              <li>
                <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-blue-800 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                  <span class="inline-flex justify-center items-center ml-4">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    </svg>
                  </span>
                  <span class="ml-2 text-sm tracking-wide truncate">Settings</span>
                </a>
              </li>
            </ul>
           
          </div>
        </div>
        <!-- ./Sidebar -->
      
        <div class="h-full ml-14 mt-2 mb-10 md:ml-64">
      
         
      
          <div class="grid grid-cols-1 lg:grid-cols-2 p-4 gap-4">
      
           <!-- component -->
<!-- This is an example component -->


        </div>

        <div class="h-full ">
 
 <div class="block md:flex">

   <div class="w-full md:w-2/5  sm:p-6 lg:p-8  ">
     <div class="flex justify-between">
       <span class="text-xl font-semibold block">Admin Profile</span>
       
     </div>

     
     <div class="w-full p-8 mx-2 flex justify-center">
       <img id="showImage" class="max-w-xs w-80 items-center rounded-lg" src="https://images.unsplash.com/photo-1477118476589-bff2c5c4cfbb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=200&q=200" alt="">    
                            
       </div>
       <div class="pl-14"><span>Upload a photo <span class="text-sm text-gray-400">(min 800x800)</span></span></div>
   </div>
   
   <div class="w-full md:w-3/5 p-8  lg:ml-4 ">
     <div class="rounded   p-6">
       <div class="pb-6">
        <span class="text-gray-200 pt-8 block opacity-70 pb-4">Personal information</span>
    
         <label for="name" class="font-semibold text-gray-300 block pb-1">Name</label>
         <div class="flex">
           <input id="name" class="border-1  rounded-r px-4 py-2 w-full" type="name" @input="$emit('update:name', $event.target.value)" />
         </div>
       </div>
       <div class="pb-4">
         <label for="about" class="font-semibold text-gray-300 block pb-1">Email</label>
         <input id="email" class="border-1  rounded-r px-4 py-2 w-full" type="email" value="example@example.com" />
         
         
       </div>
       <div class="pt-4 mr-2"></div>

      
     </div>
    
    
   </div>
   
   
   
 </div>
 <div class="ml-28"></div>
 
 

</div>

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 p-4 gap-4 pt-16 pl-56">
          <div class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group">
            <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
              <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            </div>
            <div class="text-right">
              <p class="text-2xl">69</p>
              <p>Bugs Solved</p>
            </div>
          </div>
          <div class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group">
            <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
              <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            </div>
            <div class="text-right">
              <p class="text-2xl">14</p>
              <p>Monitored Websites</p>
            </div>
          </div>
          <div class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group">
            <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
              <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
            </div>
            <div class="text-right">
              <p class="text-2xl">Aprox. 10 min</p>
              <p>Fast Report Time</p>
            </div>
          </div>
          
        </div>

          
      
       
          
      
         
      
         
      
         
        </div>
        
      </div>
      
    </div>    
    
  
    
  </template>


<script type="module">
import { getFirestore, doc, getDoc } from 'firebase/firestore';
import { ref } from 'vue';

export default {
  name: this.name,
  props: {
    name: String
  },
  data() {
    return {
      userData: null
    };
  },
  async created() {
    const app = ref();
    // Assuming you have already initialized Firebase app elsewhere
    const db = getFirestore(app.value);
    const docRef = doc(db, "users", this.name);
    const docSnap = await getDoc(docRef);
    if (docSnap.exists()) {
      this.userData = docSnap.data();
    } else {
      console.log("No such document!");
    }
  }
};
</script>