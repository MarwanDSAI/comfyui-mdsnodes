# Marwan Custom Nodes

the following custom nodes was build to use with my Ultimate Model Tester Workflow. They may also be useful for your own workflows.

ControlNet Select:
----------------- 
This node allows you to easily select a ControlNet model name and connect it directly to the Load ControlNet Model node.

Features:
Select the ControlNet model from a dropdown list.
Outputs the selected ControlNet model name as a string.
The string output can be used to store the ControlNet name in the metadata of generated images.

Ratio List Node:
---------------- 
A simple node that provides an easy way to select from predefined aspect ratios.

Features:

Choose from a list of commonly used percentage/ratio values.
Connect the output directly to any node that accepts ratio input.
Helps simplify workflow setup without manually entering values.

UNET To CKPT Converter:
-----------------------
this node allows you to use a UNET model name as a ckpt_name input for RGTHREE_CONTEXT.

Features:

Converts UNET model selection into a format compatible with ckpt_name inputs.
Useful for workflows that require model switching or compatibility with rgthree nodes.   
   
