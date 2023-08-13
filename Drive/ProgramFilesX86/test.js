class SysSystemBrightness {
    constructor(brig, id) {
        console.log(this + " Object Created On Screen " + id + "Brightness" + String(brig));

        this.brig = brig;
        this.id = id;
    }
    ChangeBrightness(number) {
        this.brig = number;
    }
    LogBrightness() {
        console.log(this.brig);
    }
    ChangeID(ids) {
        this.id = ids;
    }
    LogID() {
        console.log(this.id)
    }
}