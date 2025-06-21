class ClickButton extends React.Component {
    state = {
        wasClicked: false
    }

    handleClick () {
        this.setState(
            {wasClicked: true}
        )
    }

    render () {
        let buttonText
        if (this.state.wasClicked)
            buttonText = 'Clicked!'
        else
            buttonText = 'Click Me'
        return <button
            className="btn btn-primary mt-2"
            onClick={
                () => {
                    this.handleClick()
                }
            }
        >
            {buttonText}
        </button>
    }
}

const domContainer = document.getElementById('react_root')
ReactDOM.render(
    React.createElement(ClickButton),
    domContainer
)
