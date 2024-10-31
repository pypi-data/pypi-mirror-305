// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
  Streamlit.setComponentValue(value)
}

function buttonClick() {
  sendValue(true)
  setTimeout(sendValue(false),300)
}
/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function multiplyHeight(heightString, multiplier = 1.1) {
  // Remove the unit and convert to float
  const numericValue = parseFloat(heightString.replace(/[^0-9.-]/g, ''));

  // Multiply the numeric value
  const multipliedNumericValue = numericValue * multiplier;

  // Round to 2 decimal places for consistency
  const roundedValue = Math.round(multipliedNumericValue * 100) / 100;

  // Determine the original unit
  const unit = heightString.match(/[a-zA-Z]+$/)[0];

  // Format the result back into a string
  return `${roundedValue}${unit}`;
}

function vhToPx(vh) {
  const vhValue = parseFloat(vh.replace(/[^0-9.-]/g, ''));
  const viewportHeight = window.innerHeight || document.documentElement.clientHeight || screen.height;
  return (vhValue / 100) * viewportHeight;
}

function vwToPx(vw) {
  const vwValue = parseFloat(vw.replace(/[^0-9.-]/g, ''));
  const viewportWidth = window.innerWidth || document.documentElement.clientWidth || screen.width;
  return (vwValue / 100) * viewportWidth;
}

function getSize(size) {
  const unit = size.match(/[a-zA-Z]+$/)[0]
  let value = 0

  switch(unit) {
    case 'px':
      value = parseFloat(size.replace(/[^0-9.-]/g, ''))
      break
    case 'vw':
      value = vwToPx(size)
      break
    case 'vh':
      value = vhToPx(size)
      break
  }
  return Math.round(value)
}


function addLinkToImage(imageId, href) {
  const image = document.getElementById(imageId);
  if (image) {
    const anchor = document.createElement('a');
    anchor.href = href;
    anchor.target = '_blank';
    anchor.appendChild(image);
    anchor.color='white'
    document.body.appendChild(anchor);
  }
}

function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    // You most likely want to get the data passed in like this
    // const {input1, input2, input3} = event.detail.args

    // You'll most likely want to pass some data back to Python like this
    // sendValue({output1: "foo", output2: "bar"})
    const {key, image, label, width, height, labelColor,font_size, font_family, link} = event.detail.args;
    const obj = document.getElementById("clickable_image")
    const label_text = document.getElementById('textElement')
    const img = obj.querySelector('img')
    const height_value = getSize(height)
    if (label) {
      label_text.textContent = label
      label_text.style.color = labelColor
      label_text.style.fontSize = font_size
      label_text.style.fontFamily = font_family
    }
    if(image && height_value){
      img.src = 'data:image/png;base64,' + image
      img.style.height = height_value.toString() + 'px'
      //img.width = width
    }
    if (link){
      addLinkToImage('clickable_image', link);
    }
    //sendValue(false)
    obj.onclick = event => buttonClick()
    window.rendered = true
    Streamlit.setFrameHeight(1.1 * height_value)
  }
  else{
    sendValue(false)
  }
}

function resetValue(event) {
  sendValue(false)
}
// Render the component whenever python send a "render event"

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
//Streamlit.setFrameHeight(100)
