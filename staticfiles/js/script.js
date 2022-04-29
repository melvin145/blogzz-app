 const MenuBar=document.getElementById('icon');
 const Navlinks=document.getElementById('navlinks');
 const Closeicon=document.getElementById('close');
 MenuBar.addEventListener('click',()=>{
     Navlinks.style.display="block";
     Navlinks.style.background="#14171c";
     Navlinks.style.height="500px";
     Navlinks.style.color="black";
     Closeicon.style.display="block";
     
 })
 Closeicon.addEventListener('click',()=>{
     Navlinks.style.display="none";
     
 })