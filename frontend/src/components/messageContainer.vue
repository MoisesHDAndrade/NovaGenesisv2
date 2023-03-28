<template>
   <div>
    <top-nav-bar></top-nav-bar>
    <div class="h-100 w-100 " style="padding-top:3em">
        <div class="d-flex h-100 w-100 pb-3">
          <div class="col-12 bg-white w-100 ">
            <!-- Chat Box -->
            <div class="container p-3">
              <div class="row">
                <!-- Message Container -->
                <!-- BEGIN MAIN MESSAGE -->
                <div class="col-12">
                  <div class="card alert-info alert p-0">
                    <div class="card-body">
                      <p class="card-text">
                        We have created this space for you to send us your feedback and improvement ideas. 
                        Whether you have a suggestion for a new feature or just want to share your thoughts on the current state of the product, 
                        we're here to listen. You can directly contact us by sending a message here.<br> We look forward to hearing from you!
                      </p>
                    </div>
                  </div>
                </div>
                <!-- END MAIN MESSAGE -->
              </div>
              <div class="row " v-for="message, index in messages" :key="index">
                <!-- Message Container -->
                <div class="col-11">
                  <div class="card alert-info alert p-0">
                    <div class="card-body position-relative">
                      <div class="">
                        <p class="card-text">
                            {{ message.input }}
                        </p>
                        <div class="message-time position-absolute bottom-0 end-0">
                            <p class="text-muted m-0 p-1" style="font-size: .6em;">
                                {{  messageDate(message.date)}}
                            </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="message-row"></div>
              </div>
              <div class="row justify-content-end" v-for="message, index in messages" :key="index">
                <!-- Message Container -->
                <div class="col-11">
                  <div class="card alert-success alert p-0">
                    <div class="card-body position-relative">
                      <div class="">
                        <p class="card-text">
                            {{ message.input }}
                        </p>
                        <div class="message-time position-absolute bottom-0 end-0">
                            <p class="text-muted m-0 p-1" style="font-size: .6em;">
                                {{  messageDate(message.date)}}
                            </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="message-row"></div>
              </div>
              
              <div class="d-flex align-items-center  fixed-bottom bg-light w-100 shadow">
                <!-- Input Box -->
                <div class="col-12 px-1 ">
                  <div class="input-group my-2">
                    <input type="text" class="form-control  me-2" @keyup.enter="sendMessage()" style="height: 2em;" placeholder="Type your message..." v-model="inputMessage"/>
                    <div class="input-group-append">
                      <button class="btn btn-sm btn-warning " type="submit" @click="sendMessage()"><span class="bi bi-send"></span></button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
   </div>
</template>
<script>
import topNavBar from './TopNavBar/topNavBar.vue';
import moment from 'moment';
import {db} from './firebasedb';
import {onSnapshot, collection, doc, deleteDoc, setDoc,addDoc, orderBy, query} from 'firebase/firestore';
import {ref, onUnmounted} from 'vue';


export default {
    name:'messagecontainer',
    components:{
        topNavBar
    },
    data(){
        return{
            messages:[],
            inputMessage:""
        }
    },
    methods:{
        sendMessage(){
            this.messages.push({
                input:this.inputMessage,
                date:new Date()})
            this.playSendMessageAudio()
            this.inputMessage = ""
            setTimeout(()=>{
                this.goToBottomMessage()
            },100)
        },
        goToBottomMessage(){
            var messageRows = document.getElementsByClassName("message-row")
            if(messageRows){
            messageRows[messageRows.length -1].scrollIntoView({behavior: "smooth", block: "end", inline: "nearest", bottom:0, left:0}) 
           
            

            }
        },
        playSendMessageAudio(){
            var audio = new Audio("../../frontend/public/static/snd/bubble.wav")
            audio.play()
        },
        messageDate(date){
            return moment(date).format("DD/MM/YY - H:mm")
        }
    },
    mounted(){
        this.$root.title = "Message Box"
        document.title = "NovaGenesis | Message Box"
        const chatSnapShot = onSnapshot(
          query(collection(db,'chats'), orderBy('date','desc')),
          (snapshot)=>{
            console.log(snapshot.docs)
            snapshot.docs.map(d=>{
             
              console.log(d.data()
              )}
            )
          }

        )
    }
}
</script>