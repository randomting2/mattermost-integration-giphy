## How to
The following procedure shows how to install this project using Docker. It describes how to configure Mattermost and run the Docker image of this integration.

To install this project using Docker, you will need Docker Engine installed on your machine. Procedure to install Docker can be found [here](https://docs.docker.com/engine/installation/).

Here's how to start:

1. **Set up your Mattermost slash command**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Integrations** > **Slash Commands**
 2. Under *Add a new command*, enter `gif` into **Command Trigger Word**
 3. Paste your Web Server domain into *Callback URLs*, making sure to add `http://` to the beginning and `/new_post` to the end so it looks similar to `http://<your-web-server-domain>:<MATTERMOST_GIPHY_PORT>/new_post` and click **Add**
 4. Select `POST` method
 5. (optional) Choose a username and icon url (more details [here](https://docs.mattermost.com/developer/slash-commands.html#set-up-a-custom-command))
 6. (optional) Check the autocomplete checkbox, add `[KEYWORD]` as the hint, `Returns a GIF from Giphy based on the keyword` as the description and `Get a GIF from Giphy` as the descriptive label
 7. Copy the *Token* from your newly created slash command that appears under the *Existing commands* section

2. **Run the integration with Docker**  
  On your server, you only need to run the Docker image, with some environnement variables
    - `MATTERMOST_GIPHY_TOKEN=<your-token-here>` : this is the token you copied in the last section (you can specify multiple tokens which are separated by a colon)
    - `MATTERMOST_GIPHY_HOST=<your-host>`  : the host you want the integration (defaults to 0.0.0.0)
    - `MATTERMOST_GIPHY_PORT=<your-port-number>` : the port number you want the integration to listen on (defaults to 5000)
    - `GIPHY_API_KEY=<giphy-api-key>` : key to use for Giphy API. Default public one is `dc6zaTOxFJmzC`

  If defaults are good enough for you, simply run this command:
  ```
  docker run -d \
  --name mattermost-giphy \
  -p 5000:5000 \
  -e MATTERMOST_GIPHY_TOKEN=<your-token-here> \
  numberly/mattermost-integration-giphy
  ```

That's it! You should be able to type `gif: hello` or `/gif hello` into any channel and see a GIF from Giphy's translate service.
