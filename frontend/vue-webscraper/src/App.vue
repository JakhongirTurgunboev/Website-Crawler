<!--
An example of creating a reusable grid component and using it with external data.
-->

<script>
import DemoGrid from './Grid.vue'

export default {
  components: {
    DemoGrid
  },
  data: () => ({
    searchQuery: '',
    gridColumns: ['url', 'title'],
    gridData: [
      { url: 'Chuck Norris', title: Infinity },
      { url: 'Bruce Lee', title: 9000 },
      { url: 'Jackie Chan', title: 7000 },
      { url: 'Jet Li', title: 8000 }
    ]
  })
}
</script>

<template>
  <form id="search">
    Search Urls <input name="query" v-model="searchQuery">
  </form>
  <DemoGrid
    :data="gridData"
    :columns="gridColumns"
    :filter-key="searchQuery">
  </DemoGrid>
</template>