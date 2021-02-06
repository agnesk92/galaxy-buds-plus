<div align="center">
  <p>
    <h1>
      <a href="https://github.com/agnesk92/GalaxyBudsPlusBattery">
        <img src="icons/galaxy-small.svg" alt="Galaxy EarBuds+ App" />
      </a>
      <br />
      Galaxy EarBuds+ Battery Indicator App
    </h1>
  </p>
  <p>
    <a href="https://github.com/agnesk92/GalaxyBudsPlusBattery/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/agnesk92/galaxy-buds-plus?color=yellow&style=flat-square" alt="License" />
    </a>
  </p>
</div>

<p>
    Samsung's RFCOMM protocol interpretation for battery info was used from https://github.com/ThePBone/GalaxyBuds-BatteryLevel.
</p>

<h2>Running the app</h2>

With Conda

```
conda create -n gbuds python=3.7
conda activate gbuds
pip install -r requirements

# If it complains on missing PyGObject, use conda's binaries:
conda install -c conda-forge pygobject

# Run
python app
```

