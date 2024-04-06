<template>
<nav class=" bg-white w-full flex relative justify-between items-center mx-auto px-8 h-20">
    <!-- logo -->
    <div class="inline-flex">
       <img src="/public/logo.png" class="w-44">
    </div>

    <!-- end logo -->
    <!-- login -->
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
    <!-- end login -->
</nav>
</template>