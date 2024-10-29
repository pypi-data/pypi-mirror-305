using UnityEngine;

public class CameraShake : MonoBehaviour
{
    public Transform cameraTransform;
    private Vector3 _originalPosOfCam;
    public float shakeFrequency = 0.1f;

    void Start()
    {
        if (cameraTransform == null)
        {
            cameraTransform = Camera.main.transform;
        }
        _originalPosOfCam = cameraTransform.position;
    }

    void Update()
    {
        if (Input.GetKey(KeyCode.S))
        {
            CameraShakeEffect();
        }
        else if (Input.GetKeyUp(KeyCode.S))
        {
            StopShake();
        }
    }

    private void CameraShakeEffect()
    {
        cameraTransform.position = _originalPosOfCam + Random.insideUnitSphere * shakeFrequency;
    }

    private void StopShake()
    {
        cameraTransform.position = _originalPosOfCam;
    }
}
