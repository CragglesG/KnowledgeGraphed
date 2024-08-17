mkdir ~/.KnowledgeGraphed # Make an empty directory in the user's home directory
git clone "https://github.com/CragglesG/KnowledgeGraphed/" ~/.KnowledgeGraphed # Clone the GitHub repo into the directory
chmod +x ~/.KnowledgeGraphed/kg-make # Make kg-make executable
chmod +x ~/.KnowledgeGraphed/kg-extend # Make kg-extend executable
chmod +x ~/.KnowledgeGraphed/kg-view # Make kg-view executable
echo 'PATH=$PATH:$HOME/.KnowledgeGraphed' >>~/.bashrc # Add the directory to PATH