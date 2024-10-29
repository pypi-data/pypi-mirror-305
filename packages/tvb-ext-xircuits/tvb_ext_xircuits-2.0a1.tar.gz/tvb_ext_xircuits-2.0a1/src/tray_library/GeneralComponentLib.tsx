import { CustomNodeModel } from "../components/node/CustomNodeModel";
import { inputDialog } from "../dialog/LiteralInputDialog";
import { showFormDialog } from "../dialog/FormDialog";
import { checkInput } from "../helpers/InputSanitizer";

interface GeneralComponentLibraryProps{
    model : any;
    variableValue?: any;
}

export function cancelDialog(dialogResult) {
    if (dialogResult["button"]["label"] == 'Cancel') {
        // When Cancel is clicked on the dialog, just return
        return true;
    }
    return false
}

const TYPE_LITERALS = ['string', 'int', 'float', 'boolean', 'list', 'tuple', 'dict', 'secret', 'chat', 'numpy.ndarray'];
const TYPE_ARGUMENTS = ['string', 'int', 'float', 'boolean', 'any'];
const SPECIAL_LITERALS = ['chat'];

export async function handleLiteralInput(nodeName, nodeData, inputValue = "", type, title = "New Literal Input", nodeConnections = 0) {
    let attached = false;

    do {
        const isCreatingNewNode = nodeConnections === 0;
        type = type === 'numpy.ndarray' ? 'numpy' : type;
        let dialogOptions = inputDialog({ title, oldValue: inputValue, type, attached: (nodeData.extras?.attached || false ), showAttachOption: !isCreatingNewNode});
        let dialogResult = await showFormDialog(dialogOptions);
        if (cancelDialog(dialogResult)) return;

        if (SPECIAL_LITERALS.includes(type)) {
            // lit chat values accessed through dialogResult["value"]
            inputValue = dialogResult["value"];
        } else {
            inputValue = dialogResult["value"][title];
        }
        if(dialogResult.value.hasOwnProperty('attachNode')){
            attached = dialogResult.value.attachNode == 'on';
        }

    } while (!checkInput(inputValue, type))

    if (SPECIAL_LITERALS.includes(type)) inputValue = JSON.stringify(inputValue);
    if (nodeName === 'Literal True' || nodeName === 'Literal False') nodeName = 'Literal Boolean';

    const extras = { "type": nodeData.type, attached}
    const node = new CustomNodeModel({ name: nodeName, color: nodeData.color, extras });
    node.addOutPortEnhance({label: inputValue, name: 'out-0', dataType: nodeData.type});
    return node;
}

export async function handleArgumentInput(nodeData, argumentTitle="", oldValue="", type="argument") {
    const dialogOptions = inputDialog({ title: argumentTitle, oldValue: oldValue, type:type, inputType: nodeData.type });
    const dialogResult = await showFormDialog(dialogOptions);
    if (cancelDialog(dialogResult)) return;
    const inputValue = dialogResult["value"][argumentTitle];

    const node = new CustomNodeModel({ name: `Argument (${nodeData.type}): ${inputValue}`, color: nodeData.color, extras: { "type": nodeData.type } });
    node.addOutPortEnhance({label:'▶', name:'parameter-out-0', dataType: nodeData.type});
    return node;
}

export async function GeneralComponentLibrary(props: GeneralComponentLibraryProps){
    
    let node = null;
    let inputValue;
    const nodeData = props.model;
    const variableValue = props.variableValue || '';
    const nodeName = nodeData.task;

    // handler for Boolean
    if (nodeData.type === 'boolean' && nodeName.startsWith("Literal")) {
        const portLabel = nodeData.task.split(' ').slice(-1)[0];
        node = new CustomNodeModel({ name: "Literal Boolean", color: nodeData.color, extras: { "type": nodeData.type } });
        node.addOutPortEnhance({ label: portLabel, name: 'out-0', dataType: nodeData.type });
        return node;
    }
    
    // handler for Any
    if (variableValue) {
        const node = new CustomNodeModel({ name: nodeName, color: nodeData.color, extras: { "type": nodeData.type } });
        node.addOutPortEnhance({ label: variableValue, name: 'out-0', dataType: nodeData.type });
        return node;
    }

    if (TYPE_LITERALS.includes(nodeData.type) && nodeName.startsWith("Literal")) {
        return handleLiteralInput(nodeName, nodeData, variableValue, nodeData.type);
    }

    if (TYPE_ARGUMENTS.includes(nodeData.type)) {
        return handleArgumentInput(nodeData, 'Please define parameter');
    }

    return null;
}
