import React from 'react';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import { StreamChat } from 'stream-chat';
import { Chat, Channel, ChannelHeader, MessageInput, MessageList, Thread, Window } from 'stream-chat-react';
import 'stream-chat-css/dist/css/index.css'
import './App.css';


const chatClient = StreamChat.getInstance('uh5ay2g3z4rk');
const userToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYml0dGVyLW1vb24tMyJ9.Hj0-g7zzS_BycK6S6TGCDngG285ux0cnHWjiQROJWKw';

chatClient.connectUser(
  {
    id: 'bitter-moon-3',
    name: 'bitter-moon-3',
    image: '/img/MINDROID3.png',
  },
  userToken,
);

const channel = chatClient.channel('messaging', 'custom_channel_id', {
  // add as many custom fields as you'd like
  image: '/img/MINDROID3.png',
  name: 'Talk to Mindroid',
  members: ['bitter-moon-3'],
});


const App = () => (
  <>
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" exact />
      </Routes>
    </Router>
    <div className="text_container">
      <div className="text">
        <Chat client={chatClient} theme='messaging light'>
        <Channel channel={channel}>
          <Window>
            <ChannelHeader/>
            <MessageList/>
            <MessageInput/>
          </Window>
          <Thread/>
        </Channel>
        </Chat>
      </div>
    </div>
  </> 
);

export default App;
