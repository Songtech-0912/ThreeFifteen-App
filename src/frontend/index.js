import "./styles.css";
import Alpine from "alpinejs";

document.addEventListener('alpine:init', () => {
    Alpine.store('darkMode', {
        time: getTime()
    })
})

function getTime() {
    const current = new Date();

    const time = current.toLocaleTimeString("en-US", {
        hour: "2-digit",
        minute: "2-digit",
    });
    return time;
}

document.getElementById("app").innerHTML = `
<header>
  <!--Tabs-->
  <div id="tabs" x-data="{ tab: 'tab1' }">
    <a href="#" :class="{ 'active': tab === 'tab1' }" @click="tab = 'tab1'">All Buses</a>
    <a href="#" :class="{ 'active': tab === 'tab2' }" @click="tab = 'tab2'">Your Bus</a>
    <a href="#" :class="{ 'active': tab === 'tab3' }" @click="tab = 'tab3'">Map View</a>
    <a href="#" :class="{ 'active': tab === 'tab4' }" @click="tab = 'tab4'">Settings</a>
  <div>

  <!--Info retriever-->
  <div id="info-retrieve" x-data="{ statefactory: {} }">
    <!--<p>Latest data retrieved at: <span x-text="{ time }"></span></p>-->
  </div>
    
</header>
<main>
  <!--
  <div id="tab-container">
    <p id="tab1">
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nesciunt sunt, consectetur eos quod perferendis mollitia consequuntur natus, porro molestiae qui iusto deserunt rerum tempore voluptatum itaque. Ad, nisi esse cum quidem consequuntur ullam obcaecati. 
    </p>
    <p id="tab2"></p>
    <p id="tab3"></p>
  </div>
  -->
</main>
`;

Alpine.start();