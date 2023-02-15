// const { GatewayIntentBits, Client } = require('discord.js');

require('dotenv').config();

const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
]})

const { Configuration , OpenAIApi} = require('openai');
const configuration = new Configuration({
    organization: process.env.OPENAI_ORG,
    apiKey: process.env.OPENAI_KEY
});
const openai = new OpenAIApi(configuration);

client.on('messageCreate', async function(message){
    if(message.content.slice(-1) == '?'){
        try {
            if(message.author.bot) return;
    
            const gptResponse = await openai.createCompletion({
                model: "text-davinci-003",
                prompt: `David is a bot made by <@201227461407670272> on the work of OpenAI that reluctantly answers questions, but also lightly insults the person asking:\n\n${message.content}`,
                temperature: 0.5,
                max_tokens: 69,
                top_p: 0.3,
                frequency_penalty: 0.75,
                presence_penalty: 0.25,
            })
    
            console.log(message.content);
            message.reply(gptResponse.data.choices[0].text);
            return;
        } catch(err){
            console.log(err)
        }
    }else {
        return;
    }
});

client.login(process.env.DISCORD_TOKEN);
console.log('Logged in');