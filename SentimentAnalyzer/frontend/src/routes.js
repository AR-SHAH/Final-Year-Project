import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from './views/Main.vue'
import AddReview from './views/AddReview.vue'
import ViewReview from './views/ViewReview.vue'
import SignUp from './views/SignUp.vue'
import CheckReview from './views/CheckReview.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes:[
        {
            path:'/',
            name:'Reviews',
            component:Main,

        },
        {
            path:'/addReview',
            name:'AddReviews',
            component:AddReview,

        },
        {
            path:'/viewReview',
            name:'viewReview',
            component:ViewReview,
            props: true

        },
        {
            path:'/signup',
            name:'Signup',
            component:SignUp,
            props: true

        },
        {
            path:'/check',
            name:'CheckReview',
            component:CheckReview,
            props: true
            
        }
    ]
})