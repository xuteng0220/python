// inheritance

package com.codewithmosh;

public class Main {

    public static void main(String[] args) {
       UIControl[] controls = { new TextBox(), new CheckBox() };
       for (var control : controls)
           control.render();
    }
}



package com.codewithmosh;

public abstract class UIControl {
  private boolean isEnabled = true;

    // constructor
	// public UIControl(boolean isEnabled) {
	// this.isEnabled = isEnabled;
	// }

  public abstract void render();

  public final void enable() {
    isEnabled = true;
  }

  public void disable() {
    isEnabled = false;
  }

  // getter
  public boolean isEnabled() {
    return isEnabled;
  }
}



package com.codewithmosh;

public class TextBox extends UIControl {
  private String text = "";

	public TextBox() {
		super(true);
		System.out.println("TextBox");
	}


  @Override
  public void render() {
    System.out.println("Render TextBox");
  }

  @Override
  public String toString() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }

  public void clear() {
    text = "";
  }
}
