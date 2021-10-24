<template>
  <div>
    <h1>{{ APIData[idd]["product_id"] }}</h1>
    <h2>Total: {{totalreviews}} Postive: {{positive}} negative:{{negative}} neutral:{{neutral}}</h2>
  <textarea :value=dataInput cols="90" rows="30">
    
  </textarea>
  <h1>{{avgScore}}</h1>
 
  </div>
</template>

<script>
export default {
  name: "ViewReview",
  props: ["APIData", "idd"],
  data() {
    return {
      indexer: this.APIData[this.idd],
      avg:0,
      avgScore:"",
      dataInput:"",
      positive:0,
      negative:0,
      neutral:0,
      totalreviews:0,
    };
  },

  components: {},
    methods: {

    },
  created() {
     
                    var x=0;
                    var index =0;
                    this.indexer.reviews.forEach(e => {
                        index++;
                        if (e.score==1||e.score==2) {
                          this.positive++;
                        }
                        else if (e.score==3)
                        {
                          this.neutral++;
                        }
                        else
                        {
                          this.negative++;
                        }
                        x+=e.score;
                    });
                     this.totalreviews=index;
                     this.avg=Math.floor(x/index);
                     if (this.avg==1) {
                       this.avgScore="Best"
                     }
                     else if (this.avg==2){
                       this.avgScore="Good"
                     }
                     else if (this.avg==3){
                       this.avgScore="Normal"
                     }
                     else if (this.avg==4){
                       this.avgScore="Bad"
                     }
                     else if (this.avg==5){
                       this.avgScore="Worst"
                     }
 
                      this.indexer.reviews.forEach(e => {
                         this.dataInput+=e.review+"\n";
                    });

},

  
};
</script>

<style>
</style>
